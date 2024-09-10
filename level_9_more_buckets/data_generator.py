import lorem


def generate_posts(num_posts,flag_index):
    if flag_index >= num_posts:
        raise ValueError("flag_index should be less than num_posts")
    posts = []
    for i in range(num_posts):
        post = {
            'title': lorem.sentence(),
            'content': lorem.paragraph(),
            
        }
        if i == flag_index:
            post['flag'] = 'flag{KAUAPANGA}'
        posts.append(post)
    return posts



#if __name__ == "__main__":

    ## for testing purposes
 #   posts = generate_posts(10, 5)
  #  print(posts)