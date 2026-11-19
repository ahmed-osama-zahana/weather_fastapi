from fastapi import FastAPI 
from fastapi import Path
import json
from fastapi import HTTPException 
from pydantic import computed_field

#create a FastAPI instance
app=FastAPI()

@app.get("/home")
def home():
    return "Hello to our nursery application"


@app.get("/view")
def load_patients_data():
  with open( r"C:\Users\AHMED\Ahmed Projects\Doctor_application_fastapi\patients_data.json","r") as f:
        data=json.load(f)
  return data

@app.get("/view/{patient_id}")
def load_patient_data(patient_id:str=Path(...,description="The ID of the patient to retrieve",example="PAT-1001")):
  with open( r"C:\Users\AHMED\Ahmed Projects\Doctor_application_fastapi\patients_data.json","r") as f:
        data=json.load(f)
  for  patient in data["patients"]:
    if patient["patient_id"]==patient_id:
      return patient
  #return {"message":"Patient not found"}
  raise HTTPException(status_code=404,detail="patient not found")

# here we developing pydantic schema on http request body data contained in json 
  # class data_schema(BaseModel):
  #   var1:int
  #   var2:int


  #   @computed_field # to make this function can be seriallized and be part of transferred json 
  #   @property # to make this function can be called as argument 
  #   def calculate_weight(self):
  #      return self.var1*self.var2 