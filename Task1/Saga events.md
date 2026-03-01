|Этап|Тип события|Название|
|:-|:-:|:-:|
|Добавление товара в корзину|domain|BasketChanged|
|Доставка заказа|domain|OrderDeliveryChanged|
|Заказ подтвержден|domain|OrderSucceded|
|Заказ не прошел|compensation|OrderFailed|
|Товар забронирован|domain|OrderReservationSucceded|
|Товара нет на складе|failure|OrderReservationFailed|
|Истекло время оплаты|timeout|OrderReservationCanceled|
|Платеж подтвержден|domain|PaymentSucceded|
|Оплата не прошла|failure|PaymentFailed|
|Товар снят с резерва|compensation|PaymentFailed|
|Возврат денег|compensation|OrderFailed|
|Товар убран из корзины|compensation|OrderCanceled|
|Возврат бонусных баллов|compensation|OrderFailed|
|Разблокировать деньги на карте|compensation|OrderCanceled|
|Остановить упаковку/доставку|compensation|OrderCanceled|
|Отправить уведомление об отмене заказа|compensation|OrderCanceled|
|Отправить уведомление об ошибке оплаты|compensation|PaymentFailed|
|Отправить уведомление о возврате средств и невозможности доставки|compensation|OrderFailed|