import data
import sender_stand_request

#Зяблицев Глеб, 35-я когорта - финальный проект. Инженер по тестированию плюс
def test_order():
    creation_answer = sender_stand_request.post_new_order(data.order_body)
    track = creation_answer.json()['track']
    response = sender_stand_request.get_new_order(track)
    assert response.status_code == 200

