import random
import datetime as dt

treatments={1:"Larvae that have Tachinid flies diseases require immediate attention before the disease takes over. Usually, a single larva develops inside an individual host insect. Many tachinid larvae almost totally consume the host insect before they bore out of the host to pupate and complete the. Reducing the use of insecticides and providing sources of food like dills, parsley, clover and other herbs are the most efficient ways to conserve Trachinid flies in agricultural ecosystems (Ellis; Bradley, 1996: pp. 328-329).",2:"Larvae that have Ophryocystis diseases require immediate attention before the disease takes over. butterfly scale.The only currently known way of treating the Ophryocystis parasite is by soaking the host's eggs in a light bleach solution, which kills the spores that are present on the eggs' surface",3:"Larvae that have Nuclear polyhedrosis diseases require immediate attention before the disease takes over. Larvae were treated with nuclear polyhedrosis virus (NPV) in the laboratory to assess whether the presence of virus could potentially explain reduced fecundity observed in declining field populations of the host.",4:"The propensity of T. bourarachae to cold storage with and without diapause induction was studied. The effect of this technique on its emergence rate and parasitic activity was investigated. The study showed that wasps of T. bourarachae treated at the induction temperature of 15 °C for 5 days can be stored at 4 ± 1 °C for more than 30 days without significant loss of their performances. By using this prestorage temperature, T. bourarachae could keep its emergence capacity (77.5%) up to 60 days of cold storage at 4 ± 1 °C. However, its parasitic activity decreased significantly (37.16%) after 45 days of cold storage.",5:"Larvae that have Ophryocystis diseases require immediate attention before the disease takes over. Thoroughly dissect all species to prevent viral infections. Separate healthy larvae from the sick larvae. Clean the larval cabinet regularly. Transfer away to the safest cabinet like a new place for propagation and improve baculovirus-based pesticides is concentrated in the area of the virus genome controlling its host range."}

diseases=["Tachinid flies","Ophryocystis elektroscirrha ","Nuclear polyhedrosis","Trichogramma wasps","Baculoviruses"]

def treat():
	
	for y in treatments:
		trt=random.randint(1,5)
		if trt>=0 and trt<=4:
			today=dt.datetime.today()
			print(" Date:", today,"\n")
			print("\n DISEASES         : ",diseases[trt] )
			print(" \n TREATMENT        : \n", treatments[trt])		
treat()