from address import Address


class Mailing():
    def __init__(self,
                 to_address: Address,
                 from_address: Address,
                 cost: int,
                 track: str):
        self.to_ = to_address
        self.from_ = from_address
        self.cost = cost
        self.track = track
