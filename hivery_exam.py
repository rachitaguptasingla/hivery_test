import json

#########################################################################################
##  API Name : get_employee_details                                                    ##
##  Input    : This api expects the company_name                                       ##
##  Output   : Returns the detail of all the employees if company exists else return   ##
##             company does not exists                                                 ##
#########################################################################################
def get_employee_details(company_name):
   # Load the Employee details and Company Details using the json serializer
   with open ('./people.json') as people_details, open ('./companies.json') as company_details:
      pdata = json.load(people_details)
      cdata = json.load(company_details)
      # Fetch the company index from the cdata(company_details)
      company_id = next((comp['index'] for comp in cdata if comp['company'].casefold() == company_name.casefold()), None)
      try:
          if company_id == None:
              print(f"Company {company_name} does not exists in the companies.json")
          else:
              # Return all the details of the employees based on the company_id
              total_employees  = [ print(employee) for employee in pdata if employee['company_id'] == company_id ]
              if len(total_employees) == 0:
                 print(f"No Employees are attached with company : {company_name}:{company_id}")
      except Exception as e:
         print(f"Exception of type :{type(e).__name__} occured with arguments {e.args}")


###########################################################################################
##  API Name : get_two_employees_details                                                 ##
##  Input    : This api expects two employee name                                        ##
##  Output   : Returns Name,Age,AddreSS AND Phone of both employees                      ##
##             with the Name and index of the common friend who has brown eyes are alive ##
###########################################################################################
def common_friends(pdata, people1, people2):
    common_friend_list = [d for d in people1['friends'] if d in people2['friends']]
    for value in common_friend_list:
       index = value['index']
       [(print(f" Index : {friend['index']}"), print(f"Name : {friend['name']}")) for friend in pdata if friend['index'] == index and friend['eyeColor'].casefold() == "brown" and friend['has_died'] == False]

 
def get_two_employee_details(people1, people2):
    # Load the Employee details using the json serializer
    with open ('./people.json') as people_details:
       pdata = json.load(people_details)
    people1_data = next((people1_iter for people1_iter in pdata if people1_iter['name'] == people1), None)
    people2_data = next((people2_iter for people2_iter in pdata if people2_iter['name'] == people2), None)
    try:
        if people1_data != None and people2_data != None :
           print(f"People 1 Details: Name: {people1_data['name']}, Age: {people1_data['age']}, Address: {people1_data['address']}, Phone: {people1_data['phone']}")
           print(f"People 2 Details: Name: {people2_data['name']}, Age: {people2_data['age']}, Address: {people2_data['address']}, Phone: {people2_data['phone']}")
           print(f"Common Friends between People1 : {people1} and People2 : {people2} who are alive and have brown eyes are:")
           common_friends(pdata, people1_data, people2_data)
        else:
           print(f"Employees are not valid")
    except Exception as e:
       print(f"Exception of type :{type(e).__name__} occured with arguments {e.args}")



###########################################################################################
##  API Name : get_two_employees_details                                                 ##
##  Input    : This api expects two employee name                                        ##
##  Output   : Returns Name,Age,AddreSS AND Phone of both employees                      ##
##             with the Name and index of the common friend who has brown eyes are alive ##
###########################################################################################
def filter_veggies_fruit(pd):
    # Below are the mentioned fruits
    fruits = ['banana','strawberry','orange','apple']
    # Below are the mentioned vegetables
    veggies = ['cucumber', 'carrot', 'celery', 'beetroot']
    food = pd['favouriteFood']
    veg_list = [fInput for fInput in food if all (fd not in fInput for fd in fruits)] 
    fruit_list = [vInput for vInput in food if all (vd not in vInput for vd in veggies)] 
    return(fruit_list, veg_list)


def get_employee_food_details(people):
    # Load the Employee details using the json serializer
    with open ('./people.json') as people_details:
       pdata = json.load(people_details)
    people_detail = next((pd for pd in pdata if pd['name'] == people), None)
    try:
        if people_detail:
           (fruit,veggies) = filter_veggies_fruit(people_detail)
           dict = {"username":people_detail['name'], "age":people_detail['age'], "fruits": fruit, "vegetables": veggies}
           print(dict)
        else:
            print(f"Employee : {people} doesn't exists")
    except Exception as e:
        print(f"Exception of type :{type(e).__name__} occured with arguments {e.args}")


def main():
    # API-1 
    get_employee_details("REALMO")
    # API-2 
    get_two_employee_details("Bonnie Bass", "Decker Mckenzie")
    # API-3 
    get_employee_food_details("Bonnie Bass")



if __name__ ==  "__main__":
    main()
