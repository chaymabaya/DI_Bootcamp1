import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
data = json.loads(sampleJson)
salary = data["company"]["employee"]["payable"]["salary"]
print(f"Le salaire est : {salary}")
data["company"]["employee"]["birth_date"] = "1990-05-15"
output_file = "modified_employee.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
print(f"Le JSON modifié a été enregistré dans le fichier '{output_file}'.")
