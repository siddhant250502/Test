from fastapi import FastAPI

app = FastAPI()
@app.get("/{person}")
async def root(person):
    dict = {'aniketh':
        {'height':120,
         'Weight': 100},
        'Daali':
        {'height':120,
         'Weight': 100},
        'Thodhlesh':
        {'height':120,
         'Weight': 100}
}    
    return dict[person]
@app.get("/{surname}")
async def toor(surname):
    fname = ""
    if surname == 'jambha':
        fname='Aniketh'
    elif surname == 'Mishrikoti':
        fname='Siddhant'
    elif surname =='Mani':
        fname = 'Yashas'
    return fname    