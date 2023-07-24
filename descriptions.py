#CAT
cat= ['fat',  'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print("The description of a cat. " + size, color)
print(disposition, color)

english_name="Lime Swallowtail"
scientific_name="Papilio demoleus"
Description=["coffee-colored nasal" ,"band", "faintly visible 2 dark bands near its posterior"]

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]
        
class ButterflyFarming:
		def __init__(self):
			self.manage=None
			
		def manage_farm(self,manage):
			self.manage=manage
			steps=(manage.add_flowering_plants,manage.add_host_plants,manage.clean_farm,manage.put_butterfly_net,manage.put_butterfly,manage.add_foodplate,manage.add_oviposting_stems,manage.cagenet,manage.add_puparium,manage.add_treatment,manage.add_notification,manage.dashboard)
			[steps() for step in steps]
			
class ButterflyIdentifier:
		def __init__(self):
			self.identify=None
			
		def identify(self,identify):
			self.identify=identify
			steps=(idenify.butterfly,identify.pupa,identify.larvae,identify.eggs,identify.diseases,identify.defects)
			[steps() for step in steps]
		
			
		
