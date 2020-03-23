from aiohttp import web, ClientSession
from collections import Counter


def get_lists_intersection(first, second):
    return list((Counter(first) & Counter(second)).elements())


def get_lists_difference(first, second):
    return list((Counter(first) - Counter(second)).elements())


async def get_hh_station_list():
    hh_station_list = []
    async with ClientSession() as session:
        async with session.get('https://api.hh.ru/metro/1') as response:
            hh_station_json = await response.json()
    for lines in hh_station_json['lines']:
        for station in lines['stations']:
            hh_station_list.append(station['name'])
    return hh_station_list


routes = web.RouteTableDef()


@routes.post('/api/v1/metro/verificate')
async def metro_verificate_post(request):
    incoming_station_list = await request.json()
    hh_station_list = await get_hh_station_list()
    unchanged_stations_list = get_lists_intersection(
        incoming_station_list, hh_station_list)
    updated_stations_list = get_lists_difference(
        incoming_station_list, hh_station_list)
    deleted_stations_list = get_lists_difference(
        hh_station_list, incoming_station_list)
    return web.json_response(dict(zip(
        ['unchanged', 'updated', 'deleted'],
        [unchanged_stations_list, updated_stations_list, deleted_stations_list])))


async def init_app():
    app = web.Application()
    app.add_routes(routes)
    return app


if __name__ == '__main__':
    app = init_app()
    web.run_app(app)
