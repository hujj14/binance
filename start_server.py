import uvicorn
from faker import Faker
from main import SessionLocal, UserModel, get_password_hash, Base, engine

fake = Faker('ru_RU')

def init_db():
    print("Создание таблиц в in-memory БД...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    print("Заполнение базы сид-данными (Faker)...")
    for _ in range(10):
        user = UserModel(
            username=fake.user_name(),
            email=fake.email(),
            hashed_password=get_password_hash("password123") # Единый пароль для тестов
        )
        db.add(user)
    db.commit()
    db.close()
    print("База данных успешно заполнена 10 пользователями.")

if __name__ == "__main__":
    # 1. Инициализируем БД и заполняем данными
    init_db()
    
    # 2. Запускаем сервер (в том же процессе, поэтому in-memory база сохранится)
    print("Запуск сервера FastAPI на порту 8080...")
    uvicorn.run("main:app", host="0.0.0.0", port=8080)