class CompanyRouter:
    """
    A router to control all database operations on models in the company application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read models in the company app go to company_db.
        """
        if model._meta.app_label == 'company':
            return 'db2'  # ใช้ฐานข้อมูล db2 ซึ่งคือ company_db
        return 'default'  # ใช้ฐานข้อมูล default ซึ่งคือ employee_db

    def db_for_write(self, model, **hints):
        """
        Attempts to write models in the company app go to company_db.
        """
        if model._meta.app_label == 'company':
            return 'db2'  # เขียนไปที่ฐานข้อมูล db2 (company_db)
        return 'default'  # เขียนไปที่ฐานข้อมูล default (employee_db)

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the same database.
        """
        if obj1._meta.app_label == 'company' and obj2._meta.app_label == 'company':
            return True  # อนุญาตให้มีความสัมพันธ์ใน app company ได้
        elif obj1._meta.app_label != 'company' and obj2._meta.app_label != 'company':
            return True  # อนุญาตให้มีความสัมพันธ์ใน app อื่นได้
        return False  # ปฏิเสธความสัมพันธ์ข้ามฐานข้อมูล

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the company app only appears in the 'company_db' database.
        """
        if app_label == 'company':
            return db == 'db2'  # migrate models ของ app company ไปที่ฐานข้อมูล db2 (company_db)
        return db == 'default'  # migrate models ของ app อื่นไปที่ฐานข้อมูล default (employee_db)
