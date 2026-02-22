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