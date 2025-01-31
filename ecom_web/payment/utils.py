import random
import string


def random_string_generator(size=10, chars=string.digits):
    rand_string = ''.join(random.choice(chars) for _ in range(size))
    oid = 'OID'+ rand_string
    return oid

def unique_order_id_generator(instance):
    order_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_id= order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return order_new_id
