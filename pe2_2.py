cijferICOR = 6.6
cijferPROG = 8.0
cijferCSN = 7.5

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = gemiddelde * 30.0
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van €' + str(beloning) + ' op!'

print(overzicht)