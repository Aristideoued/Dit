#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:55:19 2021

@author: 226sauvage
"""
texte=""" En France, l'apparition des premiers articles de presse coïncide avec le développement de l'imprimerie, qui permet de diffuser des feuilles volantes comportant des « nouvelles ». À partir du xve siècle, les « occasionnels », surtout vendus par colportage, se composent d'un ou plusieurs textes consacrés à un événement (bataille, célébration, décès d'une personnalité, etc.) et illustrés par des gravures sur bois.
Les ancêtres des publications de presse telles qu'on les connaît aujourd'hui datent du début du xviie siècle, avec les premières gazettes qui rendent compte plus ou moins régulièrement de l'actualité dans des articles distincts. En 1631, La Gazette de Théophraste Renaudot publie des nouvelles de l'étranger et de la Cour. Le ton de ses articles étant jugé trop neutre ou trop soumis au pouvoir, d'autres publications font leur apparition, privilégiant les articles de commentaires. La Révolution française, qui consacre
« la libre communication de la pensée et des opinions », permet à tout citoyen d'écrire et d'imprimer librement. Les critiques et les prises de position constituent alors l'essentiel des articles de l'époque.
La Révolution industrielle et la loi sur la liberté de la presse du 29 juillet 1881 vont engendrer une nouvelle forme de journalisme. Les échos, les billets et les brèves cohabitent dans les journaux avec un nouveau genre d'article, le reportage. À la fin du xixe siècle, les quotidiens atteignent des tirages spectaculaires, Le Petit Journal (quotidien), Le Petit Parisien et Le Matin dépassant le million d'exemplaires. L'impact de certains articles est alors considérable, comme le célèbre J'accuse d'Émile Zola paru dans L'Aurore à l'occasion de l'affaire Dreyfus, ou l'enquête d'Albert Londres sur le bagne de Cayenne parue dans Le Petit Parisien.
"""
# Liste de caractères à remplacer
caract=['.',">>","(",")","»","«","'",","]

#Boucle pour remplacer caractère dans caract par un espace
for i in caract:
    texte=texte.replace(i," ")
    
# Découpage du texte en mots     
mots=texte.split()

# Affichache du texte après manipulation
print(texte)

#Affichage de la liste contenant les mots du texte
print(mots)

# Stocker le nombre de mot dans une variable puis l'afficher 
nombre_mots=len(mots)
print(nombre_mots)