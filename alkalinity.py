def monitor():
  try:
    
    val1 = 7
    val2 = 12

    alkilines = list(range(val1, val2+1))

    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < alkilines[0]):
      mesg = "Alkalinity too low!"
    elif (current > alkilines[5]):
      mesg = "Alkalinity too high!"
    else:
      mesg = "Ok"
  except:
    print("Unexpected error alkalinity") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 9