input_file = 'input1'

with open(input_file) as f:
    data = f.read().splitlines()

def run_test(test_num):
    k = int(data[(2 * test_num + 1)])
    posts = [int(x) for x in data[2 * test_num + 2].split()]
    num_posts = -1

    def set_reference_posts(point):
        marker_post = posts[point]

        distance = 1
        is_increasing = -1

        while is_increasing == -1 and point + distance < k + 1:
            ref_post = posts[point + distance]
            if ref_post > marker_post:
                is_increasing = 1
            elif ref_post < marker_post:
                is_increasing = 0
            else:
                distance += 1

        if point + distance == k + 1:
            return None, None, -1, k + 1 

        return marker_post, ref_post, is_increasing, distance

    def start_new_post(point):
        nonlocal num_posts, marker_post, ref_post, is_increasing, p
        num_posts += 1

        if point == k: # end of parcel land
            return 1

        marker_post, ref_post, is_increasing, distance = set_reference_posts(point)
        return distance

    marker_post, ref_post, is_increasing, d = set_reference_posts(0)

    p = 1 + d
    while p < k + 1:
        if is_increasing and posts[p] < ref_post:
            p += start_new_post(p)
        elif not is_increasing and posts[p] > ref_post:
            p += start_new_post(p)
        else:
            ref_post = posts[p]
            p += 1

    return num_posts

num_tests = int(data[0])

for i in range(num_tests):
    result = run_test(i)
    print(result)
