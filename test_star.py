from aitviewer.renderables.star import STARSequence
from aitviewer.viewer import Viewer


if __name__ == "__main__":
    v = Viewer()
    v.scene.add(STARSequence.t_pose())
    v.run()
