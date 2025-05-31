import logging
from typing import Any, Callable, Optional

from aiogram import F, Router
from aiogram.filters import Command, CommandStart, ExceptionTypeFilter
from aiogram.types import ErrorEvent, Message
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.api.exceptions import UnknownState

from app.bot.states import MenuState
from app.db.models import User

logger = logging.getLogger(__name__)
router = Router()


@router.message(CommandStart())
async def command_start_handler(
    message: Message,
    user: User,
    dialog_manager: DialogManager,
    i18n_format: Callable[[str, Optional[dict[str, Any]]], str],
) -> None:
    logger.info(f"[User:{user.telegram_id} ({user.name})] Opened menu")

    await dialog_manager.start(
        MenuState.menu,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.DELETE_AND_SEND,
    )


@router.error(ExceptionTypeFilter(UnknownState), F.update.message.as_("message"))
async def unknown_state_error_handler(
    event: ErrorEvent,
    message: Message,
    dialog_manager: DialogManager,
    i18n_format: Callable[[str, Optional[dict[str, Any]]], str],
    user: User,
) -> None:
    logger.warning(f"[User:{user.telegram_id} ({user.name})] Restarting dialog")

    await message.answer(i18n_format("ntf_error_unknown_state"))  # TODO: notification service

    await command_start_handler(
        message=message,
        user=user,
        dialog_manager=dialog_manager,
        i18n_format=i18n_format,
    )


@router.message(Command("test"))
async def command_test_handler(
    message: Message,
    user: User,
    dialog_manager: DialogManager,
    i18n_format: Callable[[str, Optional[dict[str, Any]]], str],
) -> None:
    logger.info(f"[User:{user.telegram_id} ({user.name})] Test command executed")

    raise UnknownState("test_state")
