def solution(players, callings):
    player_indices = {player: int(idx) for idx, player in enumerate(players)}
    for j in callings:
            idx = player_indices[j]
            player_indices[j] -= 1
            player_indices[players[idx-1]] += 1
            players[idx], players[idx - 1] = players[idx - 1], players[idx]
    return players
