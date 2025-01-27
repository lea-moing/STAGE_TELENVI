# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:03:44 2025

@author: leamo
"""

import folium

# Créer la carte centrée sur le monde
carte = folium.Map(location=[0, 0], zoom_start=2)

# Liste des stages : (lieu, coordonnées, description)
stages = [
    (
        "Centre de Géoécologie Littorale, Dinard",
        [48.6329, -2.0611],
        "Évolution du complexe écosystémique de la baie du Mont-Saint-Michel via l'imagerie optique et LiDAR à très haute résolution et la simulation hydro-sédimentaire."
    ),
    (
        "UMR 5600 EVS IRG, Bron",
        [45.7339, 4.9119],
        "Analyse hydrologique et hydro-climatologique du fonctionnement de la chaîne volcanique des Chyulu Hills au Kenya."
    ),
    (
        "LETG Rennes (CNRS), Rennes",
        [48.118402, -1.703960],
        "Adaptation des modèles de super-résolution 2D à la 3D : construction d'une base de référence de données 3D actives et passives."
    ),
    (
        "IRD, Montpellier",
        [43.645086, 3.867335],
        "Détection et segmentation des couronnes d’arbres par Deep Learning."
    ),
    (
        "INRAE - UMR DECOD, Rennes",
        [48.1146657, -1.7078647],
        "Suivi des dynamiques spatio-temporelles de l’activité phytoplanctonique dans les eaux côtières des îles Kerguelen."
    ),
    (
        "UMR SAS - INRAE, Rennes",
        [48.112868, -1.706839],
        "Étude des effets liés à la présence d’un couvert végétal sur les sols et services écosystémiques dans les vignobles en Espagne."
    ),
    (
        "UPR AIDA, CIRAD, Montpellier",
        [43.6494315, 3.8689078],
        "Évaluation spatialisée de la précision des produits globaux d’occupation du sol pour l'Afrique Sub-Saharienne."
    ),
    (
        "Ministère des armées, Paris",
        [48.8566, 2.3522],
        "Utilisation de données hyperspectrales pour les armées."
    ),
    (
        "UMIFRE 21, UAR CNRS 3330, Institut français de Pondichéry, Pondichéry, Inde",
        [11.9369164,79.8359207],
        "Cartographie des trajectoires phénologiques des cultures et des forêts sèches entre 2022 et juin 2024. Analyse des trajectoires en fonction des précipitations et de l'équilibre des ressources en eau souterraine."
    ),
    (
        "UMR TETIS, CIRAD, Montpellier",
        [43.6452586,3.8766402],
        "Analyse d'images satellitaires pour le suivi des labours motorisés dans le nord Bénin."
    ),
    (
         "BRGM, Saint-Denis, La Réunion",
         [-20.8822474,55.4487788],
         "Analyse des données EGMS (2015-2022) pour cartographier les zones mobiles, caractériser les dynamiques de déplacements, détecter des précurseurs d'effondrements récents et valider les résultats par des vérifications terrain."
    ),
    (
         "LETG Rennes (CNRS), Rennes",
         [48.1183999,-1.7038622],
         "Etudier et spatialiser l'évolution du potentiel climatique pour la viticulture en Uruguay à partir de données observées puis de données modélisées de changement climatique (SSP)."
     ),
]

# Ajouter des marqueurs pour chaque stage
for lieu, coord, description in stages:
    folium.Marker(
        location=coord,
        popup=f"<b>{lieu}</b><br>{description}",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(carte)

# Sauvegarde de la carte en fichier HTML
carte.save("C:/Users/leamo/Downloads/carte_stages_master_telenvi.html")

print("Carte créée et enregistrée sous 'carte_stages_master_telenvi.html'")
