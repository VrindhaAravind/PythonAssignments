from datetime import *

present=datetime.now()
yesterday=datetime.now()-timedelta(1)
tomorrow=datetime.now()+timedelta(1)

print("Todays date is ",present.strftime('%d-%m-%y'),", Yesterday was ",yesterday.strftime('%d-%m-%y')," and Tomorrow is ",tomorrow.strftime('%d-%m-%y'))
