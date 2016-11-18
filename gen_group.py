
def member_format(m):
    return  """ <tr> <td width="15%%"> <img src="../assets/%s"> </td>
<td> <span id="bioname"> <b> %s </b> </span>  <br>
%s
<p> %s </p>
</td>
</tr>"""%(m['image'],m['name'],m['position'],m['description'])



members=[ {"name":"Lucas Wagner","position":"Group Leader","image":"lucas.png",
    "description":"""Lucas has over a decade's experience in computing the properties of many-body quantum systems from first principles. He is the primary architect and developer of the open-source quantum Monte Carlo program QWalk, and has made advances in many-body quantum methods, as well as a number of applications to challenging electronic systems. While he has many interests, the overarching theme of his research is using computers to study systems of electrons that fall beyond the normal paradigms of metals and insulators."""},
          {"name":"Awadhesh Narayan","position":"Postdoc","image":"awadhesh-narayan_170.jpg" ,
        "description":"""Awadhesh got his PhD from Trinity College Dublin, where he studied the transport of spins in materials. His interest in this group is the prediction of new strongly correlated materials that may have quite unusual properties.
 """},
          {"name":"Kiel Williams","position":"Graduate Student","image":"kiel.png",
        "description":"""Kiel is an NSF Graduate Research Fellow who is learning how to improve many-body wave functions in realistic systems. He joined the group in summer of 2013.
 """},              
          {"name":"Brian Busemeyer","position":"Graduate Student","image":"brian.png",
        "description":"""Brian is an NSF Graduate Research Fellow who is using quantum Monte Carlo methods to study superconducting materials. He joined the group in August 2013.
 """},      
          {"name":"Jeremy Morales","position":"Associated Graduate Student","image":"profile-placeholder.gif",
        "description":"""Jeremy is a student of Peter Abbamonte who is studying magnetic models for unconventional superconductors.
 """},          
          {"name":"Li Chen","position":"Graduate Student","image":"li.png",
        "description":"""Li is studying correlated metal-insulator transitions in realistic systems. She joined the group in summer of 2014.
 """},
          {"name":"Alexander Mu&ntilde;oz",
            "position":"Graduate Student",
            "image":"Munoz.jpg",
        "description":"""Alex is joined the group in Fall 2015. He is currently working on the origin of magnetism."""},
          {"name":"William Wheeler",
            "position":"Graduate Student",
            "image":"will_wheeler.jpg",
        "description":"""William joined the group in January 2016. He is currently working on the information content of many-body wave functions, and data analysis."""},
          
                  
                  
   {"name":"Shivesh Pathak","position":"Graduate Student","image":"profile-placeholder.gif",
        "description":"""Shivesh joined the group in 2016. He is currently working on enhancing QWalk's capabilities.
 """},
          
   {"name":"Yueqing Chang","position":"Graduate Student","image":"yueqing.jpg",
        "description":"""Yueqing joined the group in fall 2016. At the time of this writing, she is still working out her project!
 """},
          
    {"name":"Kittithat (Mick) Krongchon","position":"Undergraduate Student","image":"mick.jpg",
        "description":"""Kit is working on automating electronic structure calculations in such a way that quantum Monte Carlo calculations can be performed more easily.
 """},
    {"name":"Matt Ho","position":"Undergraduate Student","image":"profile-placeholder.gif",
        "description":"""Matt is working on data-mining approaches to understanding trends in correlated electron materials. """},
    {"name":"Ping-Ko Cho",
      "position":"Undergraduate Student",
      "image":"profile-placeholder.gif",
        "description":"""Ping-Ko is working on faster implementations of QMC techniques"""
        },
    
        ]



alumni=[
          {"name":"Hitesh Changlani","position":"Postdoc","image":"hitesh.png",
        "description":"""Hitesh hails from Cornell and specializes in many-body quantum methods, mostly as applied to model lattice systems. His work in this group has focused on formalizing the link between the high energy (for condensed matter) physics of electrons and the low-energy qualitative descriptions that we use to talk about materials. Hitesh is a prolific collaborator and also worked with Shinsei Ryu, Taylor Hughes, Bryan Clark, and David Ceperley in the physics department at UIUC. He is now a postdoc at Johns Hopkins.
 """},    
          {"name":"Huihuo Zheng","position":"Graduate Student","image":"huihuo.png",
        "description":"""Huihuo has many interests, including correlated metal-insulator transitions, new methods for quantum Monte Carlo, and effective Hamiltonians. He joined the group in spring of 2012 and graduated in 2016. He is now a postdoc at Argonne National Lab.
 """},    
          {"name":"Yanbin Wu","position":"Associated Graduate Student","image":"yanbin.png",
        "description":"""Yanbin is a student of Narayan Aluru who is working with the group on calculating the interaction of water with 2D materials. He graduated in 2016 and is currently living in Houston.
 """},
          {"name":"Olabode Sule","position":"Associated Graduate Student","image":"profile-placeholder.gif",
        "description":"""Bode is a student of Shinsei Ryu who was implementing spin-orbit interactions in QWalk.
 """},
    {"name":"Jack Meister","position":"Undergraduate student","image":"profile-placeholder.gif" ,
        "description":"""Jack did his senior thesis on visualizing correlations in electronic systems.
 """},
 {"name":"Daniel Jiang","position":"Undergraduate student","image":"profile-placeholder.gif" ,
        "description":"""Daniel did some work on extending the averaging programs for QWalk.
 """},
 {"name":"Martin Graham","position":"Undergraduate student","image":"profile-placeholder.gif" ,
        "description":"""Martin did his senior thesis on improving the time step error in diffusion Monte Carlo.
 """}]

print("""---
layout: page
title: Group members
permalink: /group/
---

## Current

<table cellpadding="5" border="0" style="width:100%">
<tbody>
""")
for m in members:
  print(member_format(m))

print("""
</tbody>
</table>
""")

print("""## Alumni

<table cellpadding="5" border="0" style="width:100%">
<tbody>
""")
for a in alumni:
  print(member_format(a))
print("""
</tbody>
</table>
""")

