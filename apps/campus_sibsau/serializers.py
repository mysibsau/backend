def UnionSerializers(unions):
    result = []
    for union in unions:
        result.append({
            'name': union.name,
            'logo': union.logo,
            'photo': union.photo,
            'fio': union.fio,
            'address': union.address,
            'phone': union.phone,
            'group_vk': union.group_vk,
            'page_vk': union.page_vk
        })
    return result



def BuildingSerializers(buildings):
    result = []
    for building in buildings:
        result.append({
            'coast': building.coast,
            'name': building.name,
            'link': building.link
        })
    return result


def DirectorSerializers(directors):
    result = []
    for director in directors:
        result.append({
            'image': director.image.url,
            'name': director.name,
            'address': director.address,
            'phone': director.phone,
            'mail': director.mail
        })
    return result


def DepartmentSerializers(departments):
    result = []
    for department in departments:
        result.append({
            'name': department.name,
            'fio': department.fio,
            'address': department.address,
            'phone': department.phone,
            'mail': department.mail
        })
    return result



def SovietSerializers(soviets):
    result = []
    for soviet in soviets:
        result.append({
            'image': soviet.image.url,
            'fio': soviet.fio,
            'address': soviet.address,
            'phone': soviet.phone,
            'mail': soviet.mail
        })
    return result



def InstituteSerializers(institutes):
    result = []
    for institute in institutes:
        result.append({
            'name': institute.name,
            'short_name': institute.short_name,
            'director': DirectorSerializers([institute.director])[0],
            'departments': DepartmentSerializers(institute.departments.all()),
            'soviet': SovietSerializers([institute.soviet])[0]
        })
    return result