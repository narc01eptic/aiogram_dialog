from aiogram_dialog.widgets.kbd import ManagedCounterAdapter, Counter


async def on_text_click(
        event: CallbackQuery,
        widget: ManagedCounterAdapter,
        dialog_manager: DialogManager,
) -> None:
    await event.answer(f"Value: {widget.get_value()}")


counter = Counter(
    id="someid",
    default=0,
    max_value=1000,
    on_text_click=on_text_click,
)
