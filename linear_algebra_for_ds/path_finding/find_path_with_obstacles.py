import numpy as np
import json
from shapely.geometry import Point, Polygon, LineString
import matplotlib.pyplot as plt


def initialize_shapely_geoms(start, finish, obstacles):
    start = Point(start)
    finish = Point(finish)
    obstacles_init = []
    obstacles_shapely = []
    plt.figure(figsize=(10, 10))
    plt.axis('equal')
    line = LineString([start, finish])
    for ob in obstacles:
        ob.append(ob[0])
        obstacles_init.append(np.array(ob))
        shapely_polygon = Polygon(ob)
        obstacles_shapely.append({'distance_from_start': shapely_polygon.distance(start),
                                  'distance_to_finish': shapely_polygon.distance(finish), 'obstacle': shapely_polygon})
        x, y = zip(*ob)
        plt.plot(x, y, c='red')
    obstacles_shapely = sorted(obstacles_shapely, key=lambda k: (-k['distance_to_finish']))

    return start, finish, line, obstacles_shapely, obstacles_init


def get_line_path(start, finish, line, obstacles):
    additional_points = []
    for obstacle in obstacles:
        if line.intersects(obstacle['obstacle']):
            polin = LineString(list(obstacle['obstacle'].exterior.coords))
            points = list(polin.coords)
            test = zip(points, points[1:])
            intersection_point = obstacle['obstacle'].exterior.intersection(line)
            if intersection_point.geom_type == "MultiPoint":
                distance = []
                for point in intersection_point:
                    last = additional_points[-1] if additional_points else start
                    distance.append(Point(last).distance(point))
                inter_point = intersection_point[distance.index(min(distance))]
            else:
                inter_point = intersection_point

            # additional_points.append(inter_point.coords[0])
            for i, j in test:
                if LineString((i, j)).distance(inter_point) < 1e-8:
                    if finish.distance(Point(i)) < finish.distance(Point(j)):
                        additional_points.append(i)
                    else:
                        additional_points.append(j)
                    break
            line = LineString([start, *additional_points, finish])

    return line


def find_path(start, finish, obstacles=[]):
    start_s, finish_s, line, obstacles_shapely, obstacles_init = initialize_shapely_geoms(start, finish, obstacles)
    line = get_line_path(start_s, finish_s, line, obstacles_shapely)
    polyline = []
    x = []
    y = []
    for point in line.coords:
        polyline.append(np.array([point[0], point[1]]))
        x.append(point[0])
        y.append(point[1])
    plt.plot(x, y,  c='green')
    plt.axis('equal')
    plt.show()

    return polyline


if __name__ == '__main__':
    data_file = 'data_example.json'
    f = open(data_file)
    data = json.load(f)
    f.close()

    find_path(data["start"], data["finish"], data["obstacles"])
