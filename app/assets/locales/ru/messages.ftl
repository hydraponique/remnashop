# Used to create a blank line between elements
space = {"\u00A0"}

subscription =
    💳 Подписка: { $status ->
    [active]
    <blockquote>
    • Количество устройств: { $devices } / { $max_devices }
    • Заканчивается через: { $expiry_time }
    </blockquote>
    [expired]
    <blockquote>
    • Срок действия истёк.
    • Чтобы продлить нажмите кнопку "💳 Подписка"
    </blockquote>
    *[none]
    <blockquote>
    • У вас нет подписки
    • Чтобы купить нажмите кнопку "💳 Подписка"
    </blockquote>
}

profile =
    👤 Профиль:
    <blockquote>
    • ID: { $id }
    • Имя: { $name }
    • Баланс: { $balance }
    </blockquote>