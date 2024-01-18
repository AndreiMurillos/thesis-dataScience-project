import folium
import json

# Crea un mapa centrado en Aguascalientes
aguascalientes_map = folium.Map(location=[21.879459, -102.295606], zoom_start=10)

EstacionAgs = (21.896, -102.309)
folium.Marker(
    location=EstacionAgs,
    popup="EstacionAgs",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionAgs2 = (21.906, -102.265)
folium.Marker(
    location=EstacionAgs2,
    popup="EstacionAgs2",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionAguaZarca = (21.974, -102.584)
folium.Marker(
    location=EstacionAguaZarca,
    popup="EstacionAguaZarca",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionAlamitosCampamento = (22.178, -102.586)
folium.Marker(
    location=EstacionAlamitosCampamento,
    popup="EstacionAlamitosCampamento",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionArroyoHondo = (22.183, -102.208)
folium.Marker(
    location=EstacionArroyoHondo,
    popup="EstacionArroyoHondo",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionAsientos = (22.24, -102.089)
folium.Marker(
    location=EstacionAsientos,
    popup="EstacionAsientos",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionCalvillito = (21.835, -102.183)
folium.Marker(
    location=EstacionCalvillito,
    popup="EstacionCalvillito",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionCalvillo = (21.837, -102.712)
folium.Marker(
    location=EstacionCalvillo,
    popup="EstacionCalvillo",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionCanadaHonda = (22.001, -102.199)
folium.Marker(
    location=EstacionCanadaHonda,
    popup="EstacionCanadaHonda",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionCieneguilla = (21.731, -102.453)
folium.Marker(
    location=EstacionCieneguilla,
    popup="EstacionCieneguilla",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionCosio = (22.363, -102.297)
folium.Marker(
    location=EstacionCosio,
    popup="EstacionCosio",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionElChayote = (22.286, -102.236)
folium.Marker(
    location=EstacionElChayote,
    popup="EstacionElChayote",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionElNovillo = (22.019, -101.999)
folium.Marker(
    location=EstacionElNovillo,
    popup="EstacionElNovillo",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionElOcote = (21.783, -102.517)
folium.Marker(
    location=EstacionElOcote,
    popup="EstacionElOcote",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionElOcoteCalvillo = (21.89, -102.832)
folium.Marker(
    location=EstacionElOcoteCalvillo,
    popup="EstacionElOcoteCalvillo",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionElTule = (22.083, -102.091)
folium.Marker(
    location=EstacionElTule,
    popup="EstacionElTule",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionGanaderiaPenuelas = (21.711, -102.282)
folium.Marker(
    location=EstacionGanaderiaPenuelas,
    popup="EstacionGanaderiaPenuelas",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionJesusMaria = (21.962, -102.345)
folium.Marker(
    location=EstacionJesusMaria,
    popup="EstacionJesusMaria",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionJesusTeran = (21.976, -102.062)
folium.Marker(
    location=EstacionJesusTeran,
    popup="EstacionJesusTeran",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionLaLabor = (21.964, -102.697)
folium.Marker(
    location=EstacionLaLabor,
    popup="EstacionLaLabor",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionLaPostaUAA = (21.972, -102.362)
folium.Marker(
    location=EstacionLaPostaUAA,
    popup="EstacionLaPostaUAA",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionLaPrimavera = (21.959, -102.476)
folium.Marker(
    location=EstacionLaPrimavera,
    popup="EstacionLaPrimavera",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionLasFraguas = (22.039, -101.893)
folium.Marker(
    location=EstacionLasFraguas,
    popup="EstacionLasFraguas",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionLasPresas = (21.909, -102.087)
folium.Marker(
    location=EstacionLasPresas,
    popup="EstacionLasPresas",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionLaTinaja = (21.809, -102.13)
folium.Marker(
    location=EstacionLaTinaja,
    popup="EstacionLaTinaja",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionLaTinajaSanJose = (22.164, -102.554)
folium.Marker(
    location=EstacionLaTinajaSanJose,
    popup="EstacionLaTinajaSanJose",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionLosAlisos = (21.742, -102.717)
folium.Marker(
    location=EstacionLosAlisos,
    popup="EstacionLosAlisos",
    icon=folium.Icon(color='red')
).add_to(aguascalientes_map)

EstacionLosConos = (21.898, -101.993)
folium.Marker(
    location=EstacionLosConos,
    popup="EstacionLosConos",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionLosCuartos = (21.986, -102.35)
folium.Marker(
    location=EstacionLosCuartos,
    popup="EstacionLosCuartos",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionLosNegritos = (21.871, -102.349)
folium.Marker(
    location=EstacionLosNegritos,
    popup="EstacionLosNegritos",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionMalpaso = (21.86, -102.664)
folium.Marker(
    location=EstacionMalpaso,
    popup="EstacionMalpaso",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionMesillas = (22.313, -102.166)
folium.Marker(
    location=EstacionMesillas,
    popup="EstacionMesillas",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionMilpillasDeArriba = (21.935, -102.551)
folium.Marker(
    location=EstacionMilpillasDeArriba,
    popup="EstacionMilpillasDeArriba",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionMontoro = (21.757, -102.302)
folium.Marker(
    location=EstacionMontoro,
    popup="EstacionMontoro",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPabellonCampoEmpresarial = (22.167, -102.293)
folium.Marker(
    location=EstacionPabellonCampoEmpresarial,
    popup="EstacionPabellonCampoEmpresarial",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionPabellonDeArteaga = (22.147, -102.279)
folium.Marker(
    location=EstacionPabellonDeArteaga,
    popup="EstacionPabellonDeArteaga",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPaloAlto = (21.916, -101.969)
folium.Marker(
    location=EstacionPaloAlto,
    popup="EstacionPaloAlto",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionPenuelas = (21.726, -102.272)
folium.Marker(
    location=EstacionPenuelas,
    popup="EstacionPenuelas",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPresa50Aniversario = (22.189, -102.464)
folium.Marker(
    location=EstacionPresa50Aniversario,
    popup="EstacionPresa50Aniversario",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPresaCanutillo = (21.837, -102.522)
folium.Marker(
    location=EstacionPresaCanutillo,
    popup="EstacionPresaCanutillo",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPresaElNiagara = (21.781, -102.372)
folium.Marker(
    location=EstacionPresaElNiagara,
    popup="EstacionPresaElNiagara",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPresaJocoque = (22.128, -102.359)
folium.Marker(
    location=EstacionPresaJocoque,
    popup="EstacionPresaJocoque",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionPresaLaCodorniz = (21.997, -102.674)
folium.Marker(
    location=EstacionPresaLaCodorniz,
    popup="EstacionPresaLaCodorniz",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionPresaMediaLuna = (21.794, -102.802)
folium.Marker(
    location=EstacionPresaMediaLuna,
    popup="EstacionPresaMediaLuna",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionPresaPlutarcoEliasCalles = (22.141, -102.415)
folium.Marker(
    location=EstacionPresaPlutarcoEliasCalles,
    popup="EstacionPresaPlutarcoEliasCalles",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionPresaPotrerillos = (22.233, -102.444)
folium.Marker(
    location=EstacionPresaPotrerillos,
    popup="EstacionPresaPotrerillos",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionPuertoDeLaConcepcion = (22.203, -102.135)
folium.Marker(
    location=EstacionPuertoDeLaConcepcion,
    popup="EstacionPuertoDeLaConcepcion",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionRanchoSeco = (22.088, -101.967)
folium.Marker(
    location=EstacionRanchoSeco,
    popup="EstacionRanchoSeco",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionRanchoViejo = (22.123, -102.511)
folium.Marker(
    location=EstacionRanchoViejo,
    popup="EstacionRanchoViejo",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionRinconDeRommos = (22.231, -102.315)
folium.Marker(
    location=EstacionRinconDeRommos,
    popup="EstacionRinconDeRommos",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionSanBartolo = (21.748, -102.17)
folium.Marker(
    location=EstacionSanBartolo,
    popup="EstacionSanBartolo",
    icon=folium.Icon(color='green')
).add_to(aguascalientes_map)

EstacionSandovales = (21.882, -102.109)
folium.Marker(
    location=EstacionSandovales,
    popup="EstacionSandovales",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionSanFranciscoDeLosRomo = (22.079, -102.273)
folium.Marker(
    location=EstacionSanFranciscoDeLosRomo,
    popup="EstacionSanFranciscoDeLosRomo",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionSanGil = (22.208, -102.022)
folium.Marker(
    location=EstacionSanGil,
    popup="EstacionSanGil",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionSanIsidro = (21.779, -102.104)
folium.Marker(
    location=EstacionSanIsidro,
    popup="EstacionSanIsidro",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionTepetatillo = (22.091, -102.181)
folium.Marker(
    location=EstacionTepetatillo,
    popup="EstacionTepetatillo",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

EstacionTepezala = (22.224, -102.169)
folium.Marker(
    location=EstacionTepezala,
    popup="EstacionTepezala",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionVenadero = (21.877, -102.463)
folium.Marker(
    location=EstacionVenadero,
    popup="EstacionVenadero",
    icon=folium.Icon(color='blue')
).add_to(aguascalientes_map)

EstacionVillaJuarez = (22.101, -102.068)
folium.Marker(
    location=EstacionVillaJuarez,
    popup="EstacionVillaJuarez",
    icon=folium.Icon(color='beige')
).add_to(aguascalientes_map)

# Carga el archivo GeoJSON de Aguascalientes
# with open("aguascalientes.geojson", "r") as geojson_file:
#     aguascalientes_data = json.load(geojson_file)

# Agrega la capa GeoJSON al mapa
# folium.GeoJson(aguascalientes_data).add_to(aguascalientes_map)

# Guarda el mapa como un archivo HTML
aguascalientes_map.save("aguascalientes_state_map.html")
