from sqlalchemy.orm import Session
import model, config, schema


settings = config.get_settings()

#------------------------------- CONSUMO -------------------------------

def getConsumo(db:Session, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoByPostal(db:Session, codPostal:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).filter(model.CONSUMO.codigo_postal == codPostal).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoBySector(db:Session, sector:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO).filter(model.CONSUMO.sector == sector).order_by(model.CONSUMO.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500


#------------------------------- USER -------------------------------

def getUserByEmail(db:Session, email:str):
    try:
        return db.query(model.USER).filter(model.USER.email == email).first()
    except:return settings.ERROR_500
    
#------------------------------- CONSUMO_PREDICT -------------------------------

def getConsumoPredict(db:Session, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO_PREDICT).order_by(model.CONSUMO_PREDICT.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoPredictByPostal(db:Session, codPostal:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO_PREDICT).filter(model.CONSUMO_PREDICT.codigo_postal == codPostal).order_by(model.CONSUMO_PREDICT.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getConsumoPredictBySector(db:Session, sector:str, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.CONSUMO_PREDICT).filter(model.CONSUMO_PREDICT.sector == sector).order_by(model.CONSUMO_PREDICT.id).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
#------------------------------- EMPLEO -------------------------------

def getEmpleo(db:Session, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.EMPLEO).order_by(model.EMPLEO.fecha).limit(limit).offset(skip).all()
    except:return settings.ERROR_500
    
def getEmpleoByAñoTrimestreProvincia(db:Session, año:str, trimestre:str, provincia:str):
    #try:
        return db.query(model.EMPLEO).filter(model.EMPLEO.año == año, model.EMPLEO.trimestre == trimestre, model.EMPLEO.provincia == provincia).order_by(model.EMPLEO.fecha).all()
    #except:return settings.ERROR_500
    
def getEmpleoByCCAA(db:Session, ccaa:str):
    try:
        return db.query(model.EMPLEO).filter(model.EMPLEO.ccaa == ccaa).order_by(model.EMPLEO.id).all()
    except:return settings.ERROR_500
    

#------------------------------- LUZ_GAS_CO2_BRENT -------------------------------

def getElectricidadBrentCo2Gas(db:Session, skip:int = 0, limit:int = 100):
    try:
        return db.query(model.PREDICCION_ELECTRICIDAD).order_by(model.PREDICCION_ELECTRICIDAD.fecha).limit(limit).offset(skip).all()
    except:return settings.ERROR_500