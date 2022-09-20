#Cost estimate of equipment
Ci=int(input('Enter cost of your equipment: '))
Si=int(input(f'Enter size of your equipment: '))
Sf=int(input(f'Enter size of required equipments in same units: '))
Cf=Ci*(Sf/Si)**0.6
print(f'Cost of required equipment: {Cf}')
