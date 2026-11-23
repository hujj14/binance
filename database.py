from faker import Faker
from main import SessionLocal, UserModel, get_password_hash

fake = Faker('ru_RU')

def seed_data():
    db = SessionLocal()
    
    # Проверяем, есть ли уже пользователи
    if db.query(UserModel).first():
        print("База уже заполнена.")
        db.close()
        return

    print("Генерация тестовых пользователей...")
    for _ in range(10):
        user = UserModel(
            username=fake.user_name(),
            email=fake.email(),
            hashed_password=get_password_hash("password123") # Пароль для всех: password123
        )
        db.add(user)
    
    db.commit()
    db.close()
    print("Успешно добавлено 10 пользователей.")

if __name__ == "__main__":
    seed_data()