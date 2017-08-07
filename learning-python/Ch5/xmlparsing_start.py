# 
# Example file for parsing and processing XML
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse('samplexml.xml')

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")

    for skill in skills:
        print(skill.getAttribute('name'))

    newSkill = doc.createElement('skill')
    newSkill.setAttribute('name', 'jQuery')

    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")

    for skill in skills:
        print(skill.getAttribute('name'))



if __name__ == "__main__":
    main()


