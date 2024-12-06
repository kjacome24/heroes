from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos



class Heroe:
    db_schema = 'super_heroes'
    def __init__(self,data):
        self.id = data['id'] 
        self.nombre = data['nombre']
        self.poder = data['poder']
        self.link_img = data['link_img']
        self.bio = data['bio']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def get_all(cls):
        query = "select * from heroes;"
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        heroes = []
        for heroe in resultados:
            heroes.append(cls(heroe))
        return heroes
    
    @classmethod
    def crear(cls,data):
        query = "insert into heroes ( nombre, poder, link_img, bio) values (%(nombre)s,%(poder)s,%(link_img)s,%(bio)s );"
        return connectToMySQL(cls.db_schema).query_db(query,data)
    
    @classmethod
    def eliminar(cls,data):
        query = "delete from heroes where id=%(id)s"
        return connectToMySQL(cls.db_schema).query_db(query,data)
    
    @classmethod
    def ver(cls,data):
        query = "select * from heroes where id=%(id)s"
        superheroe = connectToMySQL(cls.db_schema).query_db(query,data)
        if superheroe:
            return cls(superheroe[0])
        return None
    
    @classmethod
    def editar(cls,data):
        query = "update heroes set nombre=%(nombre)s, poder=%(poder)s, link_img=%(link_img)s, bio=%(bio)s where id=%(id)s"
        return connectToMySQL(cls.db_schema).query_db(query,data)

