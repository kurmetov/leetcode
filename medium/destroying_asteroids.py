class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
                
            else:
                print(asteroid)
                return False
            print(mass, asteroid)

        return True