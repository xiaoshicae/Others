import redis


def create_task():
    conn = redis.Redis()
    check_set = set()

    f = open('phone.log', 'r', encoding='utf-8')
    count = 0
    b_count = 0
    for line in f:
        b_count += 1
        if b_count < 12001:
            continue
        phone = line[:-1]
        if phone in check_set:
            continue
        check_set.add(phone)
        conn.lpush('zhifubao_phone', phone)
        print(phone)
        count += 1
        # if count == 50000:
        #     break

    f.close()
    print('down!')

if __name__ == '__main__':
    create_task()
