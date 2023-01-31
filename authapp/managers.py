from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Создаем класс менеджера пользователей
class MyUserManager(BaseUserManager):
    # Создаём метод для создания пользователя
    def _create_user(self, email, first_name, last_name,  password, **extra_fields):
        # Проверяем есть ли Email
        if not email:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Email")
        # Проверяем есть ли логин
        if not first_name:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Имя")
        if not last_name:
            # Выводим сообщение в консоль
            raise ValueError("Вы не ввели Фамилию")
        # Делаем пользователя
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем всё остальное
        user.save(using=self._db)
        # Возвращаем пользователя
        return user

    # Делаем метод для создание обычного пользователя
    def create_user(self, email, first_name, last_name, password):
        # Возвращаем нового созданного пользователя
        return self._create_user(email, first_name, last_name, password)

    # Делаем метод для создание админа сайта
    def create_superuser(self, email, first_name, last_name, password):
        # Возвращаем нового созданного админа
        return self._create_user(email, first_name, last_name, password, is_staff=True, is_superuser=True)