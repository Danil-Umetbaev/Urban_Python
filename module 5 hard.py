import time
class User:
    def __init__(self, name='', password='', age=0):
        self.nickname = name
        self.password = hash(password)
        self.age = age
    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == hash(other.password)
    def __str__(self):
        return f'Пользователь {self.nickname}, возраст: {self.age}'

class Video:
    def __init__(self, title="", duration=0, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __contains__(self, item):
        return item.lower() in self.title.lower()
    def __eq__(self, item):
        return item == self.title

class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user



    def log_in(self, nick, password):
        temp = User(nick, password)
        for user in self.users:
            if user == temp:
                self.current_user = user
                break
        else:
            print("Такого пользователя нет!")

    def register(self, nick, password, age):
        new_user = User(nick, password, age)
        for user in self.users:
            if user.nickname == new_user.nickname:
                print(f"Пользователь {user.nickname} уже существует")
                break
        else:
            self.users.append(new_user)
            print("Вы зарегистрировались!")
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        self.videos.extend(list(args))

    def get_videos(self, word):
        videos = []
        for video in self.videos:
            if word in video:
                videos.append(video.title)
        return videos

    def watch_video(self, name_video):

        for video in self.videos:
            if name_video == video:
                if self.current_user is None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                    break
                elif video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    for i in range(video.duration):
                        print(i+1, end=" ")
                        time.sleep(1)
                    print()
        else:
            print("Такого видео нет!")




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

