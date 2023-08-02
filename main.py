import env
import sensors
import pygame

environment = env.buildEnvironment((600, 1200))
originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, originalMap, uncertainity = (0.5, 0.01))
environment.map.fill((0, 0, 0))
infomap = environment.map.copy()

running = True

while running:
    sensorON = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False

        if sensorON:
            position = pygame.mouse.get_pos()
            laser.position = position
            sensor_data = laser.sense_obstacles()
            if sensor_data:
                environment.dataStorage(sensor_data)
        environment.show_sensorData()
        pygame.display.update()


