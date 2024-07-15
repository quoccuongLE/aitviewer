from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.viewer import Viewer

from aitviewer.remote.renderables.smpl import RemoteSMPLSequence
from aitviewer.remote.viewer import RemoteViewer


if __name__ == "__main__":
    v = Viewer()
    v.scene.add(SMPLSequence.t_pose())
    v.run()

    # v: RemoteViewer = RemoteViewer.create_new_process()
    # m = RemoteSMPLSequence(viewer=v, poses_body=SMPLSequence.t_pose())
    # v.set_frame(1)
    # v.close_connection()
