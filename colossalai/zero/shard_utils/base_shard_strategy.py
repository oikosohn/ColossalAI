from abc import ABC, abstractmethod
from colossalai.zero.sharded_param.sharded_tensor import ShardedTensor
import torch.distributed as dist
from typing import List, Optional


class BaseShardStrategy(ABC):

    def __init__(self, process_group: Optional[dist.ProcessGroup] = None) -> None:
        """Abstract Shard Strategy. Use to shard a tensors on multiple GPUs.

        Args:
            process_group (Optional[dist.ProcessGroup], optional): the process group. Defaults to None.
        """
        self.process_group = process_group
        self.world_size = dist.get_world_size(self.process_group)
        self.local_rank = dist.get_rank(self.process_group)
        super().__init__()

    @abstractmethod
    def shard(self, tensor_list: List[ShardedTensor]):
        pass

    @abstractmethod
    def gather(self, tensor_list: List[ShardedTensor]):
        pass
