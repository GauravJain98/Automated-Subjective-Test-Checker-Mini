# data_set_2 = [
#     "Republic Day honours the date on which the Constitution of India came into effect on 26 January 1950 replacing the Government of India Act (1935) as the governing document of India",
#     "The main Republic Day celebration is held in the national capital, New Delhi, at the Rajpath before the President of India. On this day, ceremonious parades take place at the Rajpath, which are performed as a tribute to India; its unity in diversity and rich cultural heritage."
# ]
# data_set_1 = [
#     "Engineering is the creative application of science, mathematical methods, and empirical evidence to the innovation, design, construction, operation and maintenance of structures, machines, materials, devices, systems, processes, and organizations for the benefit of humankind. The discipline of engineering encompasses a broad range of more specialized fields of engineering, each with a more specific emphasis on particular areas of applied mathematics, applied science, and types of application. See glossary of engineering. "
#     "The creative application of scientific principles to design or develop structures, machines, apparatus, or manufacturing processes, or works utilizing them singly or in combination; or to construct or operate the same with full cognizance of their design; or to forecast their behavior under specific operating conditions; all as respects an intended function, economics of operation and safety to life and property."
# ]

# data_sets = [data_set_1,data_set_2]

# new_data = "Google LLC is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, search engine, cloud computing, software, and hardware. It is considered one of the Big Four technology companies, along with Amazon, Apple and Facebook.Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet.\nThe company's rapid growth since incorporation has triggered a chain of products, acquisitions, and partnerships beyond Google's core search engine (Google Search). It offers services designed for work and productivity (Google Docs, Google Sheets, and Google Slides), email (Gmail/Inbox), scheduling and time management (Google Calendar), cloud storage (Google Drive), social networking (Google+), instant messaging and video chat (Google Allo, Duo, Hangouts), language translation (Google Translate), mapping and navigation (Google Maps, Waze, Google Earth, Street View), video sharing (YouTube), note-taking (Google Keep), and photo organizing and editing (Google Photos). The company leads the development of the Android mobile operating system, the Google Chrome web browser, and Chrome OS, a lightweight operating system based on the Chrome browser. Google has moved increasingly into hardware; from 2010 to 2015, it partnered with major electronics manufacturers in the production of its Nexus devices, and it released multiple hardware products in October 2016, including the Google Pixel smartphone, Google Home smart speaker, Google Wifi mesh wireless router, and Google Daydream virtual reality headset. Google has also experimented with becoming an Internet carrier (Google Fiber, Project Fi, and Google Station).Google.com is the most visited website in the world. Several other Google services also figure in the top 100 most visited websites, including YouTube and Blogger. Google is the most valuable brand in the world as of  2017, but has received significant criticism involving issues such as privacy concerns, tax avoidance, antitrust, censorship, and search neutrality. Google's mission statement is \"to organize the world's information and make it universally accessible and useful\", and its unofficial slogan was \"Don't be evil\" until the phrase was removed from the company's code of conduct around May 2018."

# input_data [
#     [
#         ("Republic day is on 26th of january",2),
#     ],
#     [
#         ("Engineering is a field",2),
#     ]
# ]


dataset = [
    {
        "question":"What is force?",
        "max_marks":6,
        "data":{
            "train_ans":"Force can be defined as a push or a pull that changes or tends to change the motion ofan object or changes the direction or shape of an object.  It causes objects to accelerate or addto their overall pressure. In simple terms, it is a push or a pull on an object that takes placewhen two objects interact. It is the basic cause of motion from rest. It is measured in ‘Newton’(N). Newton measures the force needed to move, accelerate or speed up objects. The basicformula for it is, product of &#39;m&#39; and &#39;a&#39;, where, ‘m’ stands for the mass in kilograms and ‘a’stands for acceleration. It may also be measured in Pounds. To define the force acting upon anobject completely it not only requires the magnitude but also information regarding thedirection of the force. A force is a vector that has a direction so to represent a force in adiagram it is common to use an arrow.",
            "test":[
                ("a force is any interaction that, when unopposed, will change the motion ofan object. A force can cause an object with mass to change its velocity i.e.,to accelerate. Force can also be described intuitively as a push or a pull. A force hasboth magnitude and direction, making it a vector quantity. It is measured in the SIunit of Newton and represented by the symbol F.",2),
                ("Force can be defined as a push or a pull that changes or tends to change the state ofrest or uniform motion of an object or changes the direction or shape of an object. It ismeasured in ‘Newton’ (N). Newton measures the force needed to move, accelerate or speed upobjects. To define the force acting upon an object completely it not only requires themagnitude but also information regarding the direction of the force.",4),
                ("Force is a push or pull on an object. A force can cause an object to accelerate,slow down, remain in place, or change shape. The unit of measure for force is theNewton which is abbreviated as &quot;N&quot;. Other units of force include the dyne and thepound. Force not only has a magnitude, but it also has a direction. This makes force avector. Vectors are shown by an arrow that indicates the direction of the force and anumber that indicates the magnitude.",2.5)
            ]
        }
    }
]