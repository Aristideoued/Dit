#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:01:53 2021

@author: 226sauvage
"""
""" Veuillez créer une classe Adresse:
- attributs: rue, ville, code_postal (tous de type chaine de caractère) (tous privés)
Veuillez créer une classe Personne:
- attributs: nom, sexe (tous de type chaine de caractère) addresses de type liste d'Adresse (tous ces attributs sont privés) 
Veuillez créer une classe ListePersonne:
- attributs: personnes (de type liste de Personne) (attribut public)
- methode: find_by_nom qui prend en paramètre un nom et fait une recherche dans l'attribut personnes pour trouver si oui ou non le nom existe """

class Adress:
    def __init__(self,rue,ville,code_postal):
        
        self.__rue=rue
        self.__ville=ville
        self.__code_postal=code_postal
        
class Personn:
    def __init__(self,nom,sexe,adresse):
        self.__nom=nom
        self.__sexe=sexe
        self.__adresse=adresse
        
    def return_nom(self):
        return self.__nom
    
class ListePerson:
      def __init__(self,personnes):
          self.personnes=personnes
                
      def find_by_nom(self,nom):
          
          for i in self.personnes:
              if i.return_nom()==nom:
                 return True
              else:
                 return False
         
              
                
Ad1=Adress("aa","dd","fd")   
Ad2=Adress("ll","mm","pp")   
Ad3=Adress("kk","dd","di")   

p0=Personn("hk","F",[Ad1,Ad2])
p1=Personn("Oued","M",[Ad1,Ad2,Ad3])
p2=Personn("Traore","M",[Ad1,Ad2,Ad3])

Listp=ListePerson([p0,p1,p2])

print(Listp.find_by_nom("Oued"))
      
            
        
        