
class Openpose2d:
    def __int__(self):
        pass

    def solve(self, frame):
        return {
            'pos': [[0,0,0],
                    [1,1,1],
                    [1,1,1],
                    [1,1,1],
                    ],
            'hierarchy': {
                'root': 'root',
                'hip': 'root',
                'lhipjoint': 'hip',
            }
        }