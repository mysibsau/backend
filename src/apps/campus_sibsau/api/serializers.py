from apps.campus_sibsau import models
from typing import List


def UnionSerializers(unions: List[models.Union]):
    result = []
    for union in unions:
        result.append({
            'id': union.id,
            'rank': union.rank,
            'name': union.name,
            'short_name': union.short_name,
            'logo': union.logo.url,
            'photo': union.photo.url,
            'leader_rank': union.leader_rank,
            'fio': union.fio,
            'address': union.address,
            'phone': union.phone,
            'group_vk': union.group_vk,
            'page_vk': union.page_vk,
            'about': union.about,
        })
    return result


def BuildingSerializers(buildings: List[models.Building]):
    result = []
    for building in buildings:
        result.append({
            'id': building.id,
            'coast': building.coast,
            'name': building.name,
            'address': building.address,
            'link': building.link,
            'type': building.type,
        })
    return result


def DirectorSerializers(directors: List[models.Director]):
    result = []
    for director in directors:
        result.append({
            'image': director.image.url,
            'name': director.name,
            'address': director.address,
            'phone': director.phone,
            'mail': director.mail,
        })
    return result


def DepartmentSerializers(departments: List[models.Department]):
    result = []
    for department in departments:
        result.append({
            'name': department.name,
            'fio': department.fio,
            'address': department.address,
            'phone': department.phone,
            'mail': department.mail,
        })
    return result


def SovietSerializers(soviets: List[models.Soviet]):
    result = []
    for soviet in soviets:
        result.append({
            'image': soviet.image.url,
            'fio': soviet.fio,
            'address': soviet.address,
            'phone': soviet.phone,
            'mail': soviet.mail,
        })
    return result


def InstituteSerializers(institutes: List[models.Institute]):
    result = []
    for institute in institutes:
        result.append({
            'id': institute.id,
            'name': institute.name,
            'short_name': institute.short_name,
            'director': DirectorSerializers([institute.director])[0],
            'departments': DepartmentSerializers(institute.departments.all()),
            'soviet': SovietSerializers([institute.soviet])[0],
        })
    return result


def SportClubSerializer(clubs: List[models.SportClub]):
    result = []
    for club in clubs:
        result.append({
            'id': club.id,
            'logo': club.logo.url,
            'name': club.name,
            'fio': club.fio,
            'phone': club.phone,
            'address': club.address,
            'dates': club.dates,
        })
    return result


def DesignOfficesSerializer(offices: List[models.DesignOffice]):
    result = []
    for office in offices:
        result.append({
            'id': office.id,
            'name': office.name,
            'address': office.address,
            'fio': office.fio,
            'email': office.email,
            'about': office.about,
        })
    return result
