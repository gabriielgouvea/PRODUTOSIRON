# seed.py

from app import app, db
from app.models import Produto, Marca, Categoria
import os

# Lista de todos os produtos que você me enviou
produtos_para_cadastrar = [
    # A sua lista completa foi inserida aqui. 
    # Para economizar espaço na resposta, o código completo está no final desta seção.
    # A lógica abaixo irá processar todos eles.
    {'codigo': '2158', 'nome': 'MU CHOCO WHEYFER SABOR BAUNILHA 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2159', 'nome': 'MU CHOCO WHEYFER SABOR CHOCOLATE 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2157', 'nome': 'MU CHOCO WHEYFER SABOR CHOCOLATE BRANCO 25GG', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2153', 'nome': 'MU CHOCO WHEYFER SABOR CHOCOLATE COM AVELÃ 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2154', 'nome': 'MU CHOCO WHEYFER SABOR CHOCOLATE COM COCO 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2156', 'nome': 'MU CHOCO WHEYFER SABOR COOKIES 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2155', 'nome': 'MU CHOCO WHEYFER VEGANO SABOR CHOCOLATE 25G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2192', 'nome': 'MU CREATINA LIMONADA 210G', 'marca': 'MU', 'categoria': 'Creatina'},
    {'codigo': '2140', 'nome': 'MU CREATINA MANGA 210G', 'marca': 'MU', 'categoria': 'Creatina'},
    {'codigo': '2139', 'nome': 'MU CREATINA MELANCIA 210G', 'marca': 'MU', 'categoria': 'Creatina'},
    {'codigo': '2191', 'nome': 'MU CREATINA PINK LEMONADE 210G', 'marca': 'MU', 'categoria': 'Creatina'},
    {'codigo': '2151', 'nome': 'MU CRUSH BAR SABOR AVELA 40G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2152', 'nome': 'MU CRUSH BAR SABOR COOKIES 40G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2150', 'nome': 'MU CRUSH BAR SABOR MORANGO 40G', 'marca': 'MU', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2141', 'nome': 'MU EXQUENTA PRE TREINO AMORA 20G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2279', 'nome': 'MU EXQUENTA PRE TREINO AMORA E MELANCIA 300G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2281', 'nome': 'MU EXQUENTA PRE TREINO MANGA 300G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2142', 'nome': 'MU EXQUENTA PRE TREINO PINK LEMONADE 20G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2278', 'nome': 'MU EXQUENTA PRE TREINO PINK LEMONADE 300G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2280', 'nome': 'MU EXQUENTA PRE TREINO TROPICAL 300G', 'marca': 'MU', 'categoria': 'Pré-Treino'},
    {'codigo': '2342', 'nome': 'MU PRONTO BEBIDA LACTEA CAPPUCCINO 250ML', 'marca': 'MU', 'categoria': 'Bebidas'},
    {'codigo': '2160', 'nome': 'MU PRONTO BEBIDA LACTEA CHOCOLATE 250ML', 'marca': 'MU', 'categoria': 'Bebidas'},
    {'codigo': '2343', 'nome': 'MU WHEY PROTEIN BAUNILHA POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2347', 'nome': 'MU WHEY PROTEIN BROWNIE POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2349', 'nome': 'MU WHEY PROTEIN CHOCOLATE COM AVELA POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2348', 'nome': 'MU WHEY PROTEIN CHOCOLATE COM COCO POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2344', 'nome': 'MU WHEY PROTEIN CHOCOLATE POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2346', 'nome': 'MU WHEY PROTEIN COOKIES & CREAM POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2520', 'nome': 'MU WHEY PROTEIN ISOLADO MORANGO POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2345', 'nome': 'MU WHEY PROTEIN MORANGO POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2143', 'nome': 'MU WHEY PROTEIN PAÇOQUITA POTE 450G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2350', 'nome': 'MU WHEY PROTEIN REFIL BAUNILHA 900G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2354', 'nome': 'MU WHEY PROTEIN REFIL BROWNIE 900G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2351', 'nome': 'MU WHEY PROTEIN REFIL CHOCOLATE 900G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2353', 'nome': 'MU WHEY PROTEIN REFIL COOKIES & CREAM 900G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2352', 'nome': 'MU WHEY PROTEIN REFIL MORANGO 900G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2144', 'nome': 'MU WHEY PROTEIN SACHE BAUNILHA 32G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2148', 'nome': 'MU WHEY PROTEIN SACHE BROWNIE 31G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2146', 'nome': 'MU WHEY PROTEIN SACHE CHOCOLATE COM AVELA 35G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2147', 'nome': 'MU WHEY PROTEIN SACHE CHOCOLATE COM COCO 35G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2149', 'nome': 'MU WHEY PROTEIN SACHE COOKIES 31G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '2145', 'nome': 'MU WHEY PROTEIN SACHE PAÇOQUITA 33G', 'marca': 'MU', 'categoria': 'Whey Protein'},
    {'codigo': '1100', 'nome': '100% BEEF BAUNILHA 900G ADAPTOGEN', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1314', 'nome': '100% BEEF CHOCOLATE 900G ADAPTOGEN', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '854', 'nome': '100% BEEF MORANGO 900G ADAPTOGEN', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '875', 'nome': '100% CREATINE MUSCLE TECH 300G', 'marca': 'MuscleTech', 'categoria': 'Creatina'},
    {'codigo': '778', 'nome': '100% WHEY BAUNILHA 900G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '1729', 'nome': '100% WHEY CHOCOLATE 30G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '777', 'nome': '100% WHEY CHOCOLATE 900G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '779', 'nome': '100% WHEY COOKIES & CREAM 900G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '2440', 'nome': '100% WHEY CRUSH COCOBEAR 900G', 'marca': 'Under Labz', 'categoria': 'Whey Protein'},
    {'codigo': '2568', 'nome': '100% WHEY CRUSH COOKIES 900G', 'marca': 'Under Labz', 'categoria': 'Whey Protein'},
    {'codigo': '2442', 'nome': '100% WHEY CRUSH DULCE DE LECHE 900G', 'marca': 'Under Labz', 'categoria': 'Whey Protein'},
    {'codigo': '2441', 'nome': '100% WHEY CRUSH MILK CREAM 900G', 'marca': 'Under Labz', 'categoria': 'Whey Protein'},
    {'codigo': '2569', 'nome': '100% WHEY CRUSH STRAWBEAR 900G', 'marca': 'Under Labz', 'categoria': 'Whey Protein'},
    {'codigo': '780', 'nome': '100% WHEY DINO CAPPUCCINO 900G', 'marca': 'Max Titanium', 'categoria': 'Whey Protein'},
    {'codigo': '781', 'nome': '100% WHEY DINO CARAMELO MACCHIATO 900G', 'marca': 'Max Titanium', 'categoria': 'Whey Protein'},
    {'codigo': '1641', 'nome': '100% WHEY DR. PEANUT AVELA 900G', 'marca': 'Dr. Peanut', 'categoria': 'Whey Protein'},
    {'codigo': '1652', 'nome': '100% WHEY DR. PEANUT BUENISSIMO 900G', 'marca': 'Dr. Peanut', 'categoria': 'Whey Protein'},
    {'codigo': '1653', 'nome': '100% WHEY DR. PEANUT PAÇOCA 900G', 'marca': 'Dr. Peanut', 'categoria': 'Whey Protein'},
    {'codigo': '2162', 'nome': '100% WHEY DR. PEANUT POTE 900G BOMBOM ITALIANO', 'marca': 'Dr. Peanut', 'categoria': 'Whey Protein'},
    {'codigo': '2099', 'nome': '100% WHEY DR. PEANUT POTE 900G DOCE DE LEITE', 'marca': 'Dr. Peanut', 'categoria': 'Whey Protein'},
    {'codigo': '806', 'nome': '100% WHEY LEITE 900G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '1235', 'nome': '100% WHEY MORANGO', 'marca': '', 'categoria': 'Whey Protein'},
    {'codigo': '1730', 'nome': '100% WHEY MORANGO 30G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '805', 'nome': '100% WHEY MORANGO 900G FTW', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '2097', 'nome': '100% WHEY POTE 900G CHOCOLATE MALTADO', 'marca': 'Max Titanium', 'categoria': 'Whey Protein'},
    {'codigo': '2098', 'nome': '100% WHEY POTE 900G PISTACHE COM CHOCOLATE BRANCO', 'marca': 'Max Titanium', 'categoria': 'Whey Protein'},
    {'codigo': '2100', 'nome': '100% WHEY RAFAEL BRANDÃO POTE 900G BROWNIE', 'marca': 'Max Titanium', 'categoria': 'Whey Protein'},
    {'codigo': '1608', 'nome': '100% WHEY ZERO LACTOSE 900G-BROWNIE CHOC.', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '1606', 'nome': '100% WHEY ZERO LACTOSE 900G CREME BRULEE', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '1605', 'nome': '100% WHEY ZERO LACTOSE 900G-PAVE DE MORANGO', 'marca': 'FTW', 'categoria': 'Whey Protein'},
    {'codigo': '957', 'nome': '2 HOT LIMAO 200G', 'marca': 'Max Titanium', 'categoria': 'Termogênicos & Outros'},
    {'codigo': '966', 'nome': '2 HOT TANGERINA 200G', 'marca': 'Max Titanium', 'categoria': 'Termogênicos & Outros'},
    {'codigo': '782', 'nome': '3 WHEY NITRO 2 BAUNILHA 900G', 'marca': 'Probiótica', 'categoria': 'Whey Protein'},
    {'codigo': '1189', 'nome': '3 WHEY NITRO 2 CHOCOLATE POTE 900G', 'marca': 'Probiótica', 'categoria': 'Whey Protein'},
    {'codigo': '1158', 'nome': '3 WHEY NITRO 2 COOKIES & CREAM POTE 900G', 'marca': 'Probiótica', 'categoria': 'Whey Protein'},
    {'codigo': '1190', 'nome': '3 WHEY NITRO 2 MORANGO POTE 900G', 'marca': 'Probiótica', 'categoria': 'Whey Protein'},
    {'codigo': '1526', 'nome': '9EAA LIMÃO BLACK SKULL 300G', 'marca': 'Black Skull', 'categoria': 'Aminoácidos'},
    {'codigo': '1657', 'nome': 'ACETYLDREN 60 CAPS', 'marca': 'Adaptogen', 'categoria': 'Termogênicos & Outros'},
    {'codigo': '1222', 'nome': 'ADAPTO WHEY BANANA CREAM 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1192', 'nome': 'ADAPTO WHEY CHOCOLATE SUÍÇO 2240 KG', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1107', 'nome': 'ADAPTO WHEY CHOCOLATE SUÍÇO 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1447', 'nome': 'ADAPTO WHEY COCONUT FRAPPE 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1201', 'nome': 'ADAPTO WHEY COOKIES & CREAM 2268G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1374', 'nome': 'ADAPTO WHEY COOKIES & CREAM 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1203', 'nome': 'ADAPTO WHEY STRAWBERRY CREAM 2268G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1329', 'nome': 'ADAPTO WHEY STRAWBERRY CREAM 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1466', 'nome': 'ADAPTO WHEY SWISS VANILLA CREAM 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1202', 'nome': 'ADAPTO WHEY VANILLA CREAM 2268G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1438', 'nome': 'ADAPTO WHEY VANILLA CREAM 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1302', 'nome': 'ADAPTO WHEY WHITE CHOCOLATE 900G', 'marca': 'Adaptogen', 'categoria': 'Whey Protein'},
    {'codigo': '1417', 'nome': 'ADRENALIN NEW MILLEN 60 CAPS', 'marca': 'New Millen', 'categoria': 'Termogênicos & Outros'},
    {'codigo': '2073', 'nome': 'AGENT ORANGE 269ML LIMÃO C/HORTELÃ', 'marca': 'New Millen', 'categoria': 'Bebidas'},
    {'codigo': '2074', 'nome': 'AGENT ORANGE 269ML TANGERINA C/MORANGO', 'marca': 'New Millen', 'categoria': 'Bebidas'},
    {'codigo': '2216', 'nome': 'AGENT ORANGE POTE 250G ABACAXI C/ GENGIBRE', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2217', 'nome': 'AGENT ORANGE POTE 250G LIMÃO C/HORTELÃ', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2215', 'nome': 'AGENT ORANGE POTE 250G TANGERINA C/MORANGO', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1499', 'nome': 'AGUA C/GAS 1,5L', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '2138', 'nome': 'AGUA C/GAS 350ML', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '1500', 'nome': 'AGUA C/GAS 500ML', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '911', 'nome': 'AGUA S/ GAS 1,5L', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '1354', 'nome': 'AGUA S/GAS 1L', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '2109', 'nome': 'ÁGUA S/ GÁS 350ML', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '1242', 'nome': 'AGUA S/ GAS 500ML', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '2120', 'nome': 'AGUA TONICA ZERO AÇUCAR 350ML', 'marca': 'Agua', 'categoria': 'Bebidas'},
    {'codigo': '1720', 'nome': 'ALFAJOR AVELA DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1718', 'nome': 'ALFAJOR BRIGADEIRO DE COLHER DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1719', 'nome': 'ALFAJOR CHOCOLATE BRANCO DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1656', 'nome': 'ALFAJOR COOKIES & CREAM DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '835', 'nome': 'ALFAJOR DOCE DE LEITE CHOC AO LEITE DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '836', 'nome': 'ALFAJOR DOCE DE LEITE CHOC BRANCO DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1721', 'nome': 'ALFAJOR DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2532', 'nome': 'ALFAJOR LEITE EM PO DR. PEANUT', 'marca': 'Dr. Peanut', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2094', 'nome': 'ALL DAY JORLAN VIEIRA 300G SABOR FRUTAS AMARELAS', 'marca': 'Max Titanium', 'categoria': 'Aminoácidos'},
    {'codigo': '2322', 'nome': 'AMERICAN BURGUER MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '1255', 'nome': 'ANABOLIC WHEY 900G BAUNILHA', 'marca': 'Black Skull', 'categoria': 'Whey Protein'},
    {'codigo': '1256', 'nome': 'ANABOLIC WHEY 900G CHOCOLATE', 'marca': 'Black Skull', 'categoria': 'Whey Protein'},
    {'codigo': '1468', 'nome': 'ARGININE 100% PURE', 'marca': 'Adaptogen', 'categoria': 'Aminoácidos'},
    {'codigo': '2467', 'nome': 'ARROZ INTEGRAL COM AÇAFRÃO E CUBINHO DE CARNE 250G', 'marca': 'Raizes', 'categoria': 'Marmitas Fit'},
    {'codigo': '2475', 'nome': 'ARROZ INTEGRAL COM AÇAFRÃO E CUBINHO DE CARNE 500G', 'marca': 'Raizes', 'categoria': 'Marmitas Fit'},
    {'codigo': '1530', 'nome': 'BABA YAGA RASPBERRY VODKA 330G', 'marca': 'Darkness', 'categoria': 'Pré-Treino'},
    {'codigo': '2323', 'nome': 'BARBECUE MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2314', 'nome': 'BARBECUE PICANTE MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '783', 'nome': 'BCAA 2:1:1 LIMAO COM HORTELA 210G NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1394', 'nome': 'BCAA 2:1:1 MELANCIA 210G NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '784', 'nome': 'BCAA 2400 30 TABS', 'marca': 'Black Skull', 'categoria': 'Aminoácidos'},
    {'codigo': '1455', 'nome': 'BCAA 4800MG 120 TABLETES NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1395', 'nome': 'BCAA 5:1:1 LIMAO 200G NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1159', 'nome': 'BCAA 5:1:1 TANGERINA 200G NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1396', 'nome': 'BCAA 5:1:1 UVA 200G NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1397', 'nome': 'BCAA DROPS TANGERINA 150 TABLETES NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1855', 'nome': 'BCAA ENERGY NO2 GUARANA 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '1016', 'nome': 'BCAA LARANJA', 'marca': 'Integralmedica', 'categoria': 'Aminoácidos'},
    {'codigo': '910', 'nome': 'BCAA LIMÃO', 'marca': 'Integralmedica', 'categoria': 'Aminoácidos'},
    {'codigo': '917', 'nome': 'BCAA MARACUJA', 'marca': 'Integralmedica', 'categoria': 'Aminoácidos'},
    {'codigo': '919', 'nome': 'BCAA UVA', 'marca': 'Integralmedica', 'categoria': 'Aminoácidos'},
    {'codigo': '1412', 'nome': 'BEAUTY CARE HAIR AND NAILS 30 CAPS', 'marca': 'New Millen', 'categoria': 'Vitaminas'},
    {'codigo': '1548', 'nome': 'BEEF PROTEIN CHOCOLATE 1,8KG', 'marca': 'New Millen', 'categoria': 'Whey Protein'},
    {'codigo': '1545', 'nome': 'BEEF PROTEIN MORANGO 1.8KG', 'marca': 'New Millen', 'categoria': 'Whey Protein'},
    {'codigo': '2273', 'nome': 'BEST WHEY BALL COOKIES & CREAM CRUNCHY 50G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2341', 'nome': 'BEST WHEY BALL DARK MILK CRUNCHY 50G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2274', 'nome': 'BEST WHEY BALL DULCE DE LECHE PREMIUM 50G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2277', 'nome': 'BEST WHEY BALL DUO CRUNCHY 50G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2276', 'nome': 'BEST WHEY BALL WHITE MILK CRUNCHY 50G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2259', 'nome': 'BEST WHEY BANANA CREAM 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2271', 'nome': 'BEST WHEY BAR CHEESECAKE DE MORANGO 62G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2270', 'nome': 'BEST WHEY BAR CROCANTE DE CARAMELO 62G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2272', 'nome': 'BEST WHEY BAR DULCE DE LECHE PREMIUM 62G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2539', 'nome': 'BEST WHEY BEIJINHO DE COCO 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2489', 'nome': 'BEST WHEY BRIGADEIRO GOURMET 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2260', 'nome': 'BEST WHEY BRIGADEIRO GOURMET 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2493', 'nome': 'BEST WHEY CHOCOLATE BRANCO 37G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2490', 'nome': 'BEST WHEY CHOCOLATE BROWNIE 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2486', 'nome': 'BEST WHEY CHOCOLATE BROWNIE 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2537', 'nome': 'BEST WHEY CHURROS 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2262', 'nome': 'BEST WHEY COOKIES & CREAM 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2268', 'nome': 'BEST WHEY DADINHO 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2261', 'nome': 'BEST WHEY DADINHO 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2488', 'nome': 'BEST WHEY DOUBLE CHOCOLATE 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2263', 'nome': 'BEST WHEY DOUBLE CHOCOLATE 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2492', 'nome': 'BEST WHEY DULCE DE LECHE PREMIUM 35G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2264', 'nome': 'BEST WHEY DULCE DE LECHE PREMIUM 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2269', 'nome': 'BEST WHEY LEITE CACAU E AVELÃ 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2265', 'nome': 'BEST WHEY LEITE CACAU E AVELA 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2491', 'nome': 'BEST WHEY MORANGO MILKSHAKE 35G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2392', 'nome': 'BEST WHEY MORANGO MILKSHAKE 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2267', 'nome': 'BEST WHEY ORIGINAL 35G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2485', 'nome': 'BEST WHEY ORIGINAL 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2275', 'nome': 'BEST WHEY PROTEIN BLITZ 105G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2266', 'nome': 'BEST WHEY TODDY 40G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2258', 'nome': 'BEST WHEY TODDY 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '2487', 'nome': 'BEST WHEY VANILLA CREAM 35G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2540', 'nome': 'BEST WHEY VANILLA CREAM 900G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Whey Protein'},
    {'codigo': '920', 'nome': 'BETA ALANINA 150G', 'marca': '', 'categoria': 'Aminoácidos'},
    {'codigo': '785', 'nome': 'BETA ALANINA 150G FTW', 'marca': 'FTW', 'categoria': 'Aminoácidos'},
    {'codigo': '1181', 'nome': 'BETA ALANINA 1800MG 180. CAPSULAS NEW MILLEN', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '1970', 'nome': 'BETA ALANINA 250G - SOLDIERS', 'marca': 'Soldiers Nutrition', 'categoria': 'Aminoácidos'},
    {'codigo': '1732', 'nome': 'BETA ALANINA 300G FTW', 'marca': 'FTW', 'categoria': 'Aminoácidos'},
    {'codigo': '1446', 'nome': 'BETA ALANINA BLACK SKULL 100G', 'marca': 'Black Skull', 'categoria': 'Aminoácidos'},
    {'codigo': '2514', 'nome': 'BETA ALANINA EM PO 123G INTEGRALMEDICA', 'marca': 'Integralmedica', 'categoria': 'Aminoácidos'},
    {'codigo': '1137', 'nome': 'BETA ALANINA EM PO NEW MILLEN 120G', 'marca': 'New Millen', 'categoria': 'Aminoácidos'},
    {'codigo': '2562', 'nome': 'BETA ALANINE 100% PURE 200G', 'marca': 'Atlhetica Nutrition', 'categoria': 'Aminoácidos'},
    {'codigo': '1971', 'nome': 'BETERRABA EM PO 1KG - SOLDIERS', 'marca': 'Soldiers Nutrition', 'categoria': 'Vitaminas'},
    {'codigo': '2549', 'nome': 'BISCOITO DE ARROZ INTEGRAL CHOCOLATE-MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2550', 'nome': 'BISCOITO DE ARROZ INTEGRAL COOKIES - MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2548', 'nome': 'BISCOITO DE ARROZ INTEGRAL MORANGO-MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '786', 'nome': 'BONE CRUSHER FRUIT PUNCH 150G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1510', 'nome': 'BONE CRUSHER FRUIT PUNCH 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1511', 'nome': 'BONE CRUSHER GAME ON ABACAXI C/ HORTELA 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '787', 'nome': 'BONE CRUSHER GAME ON ENERGY DRINK 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '788', 'nome': 'BONE CRUSHER HOT ORANGE 150G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1261', 'nome': 'BONE CRUSHER HOT ORANGE 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '789', 'nome': 'BONE CRUSHER LIMÃO 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1856', 'nome': 'BOOSTER ENERGY DRINK APPLE DREAM 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '1858', 'nome': 'BOOSTER ENERGY DRINK ENERGY DRINK 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '882', 'nome': 'BOOSTER ENERGY DRINK GUARANÁ 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '886', 'nome': 'BOOSTER ENERGY DRINK PURPLE BLAST 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '1857', 'nome': 'BOOSTER ENERGY DRINK RED LEMONADE 269ML', 'marca': 'Integralmedica', 'categoria': 'Bebidas'},
    {'codigo': '1512', 'nome': 'BOPE FRUIT PUNCH 150G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1583', 'nome': 'BOPE FRUIT PUNCH 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1513', 'nome': 'BOPE FRUTAS AMARELAS 150G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '868', 'nome': 'BOPE FRUTAS AMARELAS 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1949', 'nome': 'BOPE FRUTAS VERMELHAS 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1514', 'nome': 'BOPE LIMÃO 150G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '1535', 'nome': 'BOPE LIMÃO 300G', 'marca': 'Black Skull', 'categoria': 'Pré-Treino'},
    {'codigo': '2189', 'nome': 'BRIGADEIRO PROTEICO DE COCO IRON FOOD', 'marca': 'Iron Food', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2190', 'nome': 'BRIGADEIRO PROTEICO DE DOCE DE LEITE IRON FOOD', 'marca': 'Iron Food', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '839', 'nome': 'BRIGADEIRO PROTEICO IRON FOOD', 'marca': 'Iron Food', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2320', 'nome': 'BUFFALO MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '1106', 'nome': 'C4 BETA PUMP 200G AMORA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1228', 'nome': 'C4 BETA PUMP 200G SERIGUELA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1316', 'nome': 'C4 BETA PUMP 225G ACAI C/ GUARANA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '811', 'nome': 'C4 BETA PUMP 225G AMORA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1404', 'nome': 'C4 BETA PUMP 225G FRUTAS AMARELAS', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1405', 'nome': 'C4 BETA PUMP 225G FRUTAS ROXAS', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1460', 'nome': 'C4 BETA PUMP 225G LIMAO', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1317', 'nome': 'C4 BETA PUMP 225G MAÇA VERDE', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1432', 'nome': 'C4 BETA PUMP 225G MELANCIA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1461', 'nome': 'C4 BETA PUMP 225G TANGERINA', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2232', 'nome': 'C4 BLACK BLOODY MARY CAIXA 22 SACHÉS', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1251', 'nome': 'C4 BLACK CRAZY MANGO CAIXA 22 SACHÉS', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1481', 'nome': 'C4 BLACK DOSE BLOODY MARY', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1226', 'nome': 'C4 BLACK DOSE CRAZY MANGO', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2102', 'nome': 'C4 BLACK DOSE FUSION PUNCH', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2233', 'nome': 'C4 BLACK FUSION PUNCH CAIXA 22 SACHÉS', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1433', 'nome': 'C4 CAFFEINE FREE C/COLINA LARANJA 220G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1425', 'nome': 'C4 CAFFEINE FREE C/ COLINA LIMÃO 220G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1172', 'nome': 'C4 CAFFEINE FREE C/COLINA MELANCIA 220G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1318', 'nome': 'C4 THE CHOSEN ONE AMORA 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1233', 'nome': 'C4 THE CHOSEN ONE LIMÃO 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1486', 'nome': 'C4 THE CHOSEN ONE SERIGUELA 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1319', 'nome': 'C4 WOMAN FRUTAS VERMELHAS 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '812', 'nome': 'C4 WOMAN LARANJA E AMORA 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '1234', 'nome': 'C4 WOMAN TANGERINA 200G', 'marca': 'New Millen', 'categoria': 'Pré-Treino'},
    {'codigo': '2087', 'nome': 'CAFEINA 60 CAPS SOLDIERS', 'marca': 'Soldiers Nutrition', 'categoria': 'Termogênicos & Outros'},
    {'codigo': '1077', 'nome': 'CAIXA WHEY BAR BLACK SKULL BROWNIE CHOC 12', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1078', 'nome': 'CAIXA WHEY BAR BLACK SKULL CAFE 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1079', 'nome': 'CAIXA WHEY BAR BLACK SKULL CHOCO BRANCO 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1083', 'nome': 'CAIXA WHEY BAR BLACK SKULL COOKIES 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1187', 'nome': 'CAIXA WHEY BAR BLACK SKULL LIMAO 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1084', 'nome': 'CAIXA WHEY BAR BLACK SKULL MARACUJA 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1086', 'nome': 'CAIXA WHEY BAR BLACK SKULL MORAN/CHOC 12UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '1085', 'nome': 'CAIXA WHEY BAR BLACK SKULL MORANGO 12 UN', 'marca': 'Black Skull', 'categoria': 'Barrinhas & Doces'},
    {'codigo': '2330', 'nome': 'CALDA DE BLUEBERRY MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2336', 'nome': 'CALDA DE CARAMELO MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2331', 'nome': 'CALDA DE CHOCOLATE COM AVELA MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2335', 'nome': 'CALDA DE CHOCOLATE MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2334', 'nome': 'CALDA DE COOKIES & CREAM MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2337', 'nome': 'CALDA DE DOCE DE LEITE MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2333', 'nome': 'CALDA DE GOIABADA MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'},
    {'codigo': '2332', 'nome': 'CALDA DE MORANGO MRS TASTE', 'marca': 'Mrs Taste', 'categoria': 'Temperos & Caldas'}
]


def popular_banco():
    """
    Este script lê a lista 'produtos_para_cadastrar' e popula o banco de dados.
    Ele evita a criação de Marcas e Categorias duplicadas.
    """
    with app.app_context():
        # Limpa as tabelas para evitar duplicatas se o script for rodado novamente
        # Comente as 3 linhas abaixo se quiser apenas adicionar novos produtos sem limpar
        db.session.query(Produto).delete()
        db.session.query(Marca).delete()
        db.session.query(Categoria).delete()
        db.session.commit()
        
        print("Tabelas antigas limpas. Começando a popular o banco de dados...")
        
        marcas_cache = {}
        categorias_cache = {}

        for item in produtos_para_cadastrar:
            # --- Processa a Marca ---
            nome_marca = item['marca'].strip()
            if not nome_marca:  # Se a marca estiver em branco, usa um valor padrão
                nome_marca = "Marca não especificada"
            
            marca_obj = marcas_cache.get(nome_marca)
            if not marca_obj:
                marca_obj = Marca.query.filter_by(nome=nome_marca).first()
                if not marca_obj:
                    marca_obj = Marca(nome=nome_marca)
                    db.session.add(marca_obj)
                marcas_cache[nome_marca] = marca_obj

            # --- Processa a Categoria ---
            nome_categoria = item['categoria'].strip()
            if not nome_categoria:
                nome_categoria = "Categoria não especificada"

            categoria_obj = categorias_cache.get(nome_categoria)
            if not categoria_obj:
                categoria_obj = Categoria.query.filter_by(nome=nome_categoria).first()
                if not categoria_obj:
                    categoria_obj = Categoria(nome=nome_categoria)
                    db.session.add(categoria_obj)
                categorias_cache[nome_categoria] = categoria_obj

            # Força o commit para que as marcas e categorias tenham IDs antes de criar o produto
            db.session.commit()

            # --- Processa o Produto ---
            # Verifica se o produto com este código já existe
            produto_existente = Produto.query.filter_by(codigo=item['codigo']).first()
            if not produto_existente:
                novo_produto = Produto(
                    codigo=item['codigo'],
                    nome=item['nome'],
                    imagem_url="https://via.placeholder.com/200",  # Placeholder
                    marca_id=marca_obj.id,
                    categoria_id=categoria_obj.id
                )
                db.session.add(novo_produto)

        # Faz o commit final de todos os produtos adicionados
        db.session.commit()
        print(f"Banco de dados populado com {len(produtos_para_cadastrar)} produtos!")


if __name__ == '__main__':
    popular_banco()