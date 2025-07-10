from typing import List

def examine_coil(master_coil_weight: float, scrap_percent: float = .01, cost: float = 15):

    return cost, master_coil_weight * scrap_percent

def trimmming(examine_scrap_weight: float,
              master_coil_weight: float, 
              master_coil_width: float, 
              width_cropped: float = 1, 
              cost: float = 15):

    scrap_percent = width_cropped / master_coil_width

    scrap_percent = .01
    # 1 percent

    scrap_weight = (master_coil_weight - examine_scrap_weight) * scrap_percent

    return cost, scrap_weight

def pickle_and_oil(master_coil_weight: float,
                   examine_scrap_weight: float, 
                   trimming_scrap_weight: float, 
                   scrap_percent: float = .01, 
                   cost: float = 15):
    
    scrap_weight = (master_coil_weight - examine_scrap_weight - trimming_scrap_weight) * scrap_percent

    return  cost, 150

def coating(master_coil_weight: float,
            examine_scrap_weight: float, 
            trimming_scrap_weight: float, 
            pickle_scrap_weight: float,
            scrap_percent: float = .01, 
            cost: float = 15):

    scrap_weight = (master_coil_weight - examine_scrap_weight - trimming_scrap_weight - pickle_scrap_weight) * scrap_percent
    
    return  cost, scrap_weight

def slitting(master_coil_width: float,
            master_coil_weight: float,
            examine_scrap_weight: float, 
            trimming_scrap_weight: float, 
            pickle_scrap_weight: float,
            coating_scrap_weight: float,
            width_per_cut: float = 1,
            num_cuts_needed: int = 1,
            scrap_percent: float = .01, 
            width_cropped: float = 1,
            cost: float = 15):
    
    updated_weight = master_coil_weight - examine_scrap_weight - trimming_scrap_weight - pickle_scrap_weight - coating_scrap_weight

    weight_per_cut = ((width_per_cut / num_cuts_needed) / (master_coil_width - width_cropped)) * updated_weight

    # scrap_weight = updated_weight - weight_per_cut

    scrap_weight = updated_weight * scrap_percent

    return cost, scrap_weight

def slitting_v2(
        master_coil_width: float,
        master_coil_weight: float,
        examine_scrap_weight: float, 
        trimming_scrap_weight: float, 
        pickle_scrap_weight: float,
        coating_scrap_weight: float,
        widths_per_cut: List[float] = [5],
        num_cuts_needed: List[float] = [1],
        width_cropped: float = 1,
        cost: float = 15):

    
    updated_weight = master_coil_weight - examine_scrap_weight - trimming_scrap_weight - pickle_scrap_weight - coating_scrap_weight
    
    used_weight = sum(((w * nc)/(master_coil_width - width_cropped)) * updated_weight for w, nc in zip(widths_per_cut, num_cuts_needed))
    scrap_weight = updated_weight - used_weight

    return cost, scrap_weight
    

def cut_to_length(
    percent: float,
    widths_per_cut: List[float],
    num_cuts_needed: List[int],
    total_weight: float,
    master_coil_width: float,
    cost: float = 15.0
):
    """
    For each slit, calculate its weight, split into equal pieces by percent, round each, and sum the leftover as scrap.
    """
    import math
    total_scrap = 0
    n_splits = int(1 / percent)
    for width, num_cuts in zip(widths_per_cut, num_cuts_needed):
        slit_weight = (width / master_coil_width) * total_weight * num_cuts
        split_weight = slit_weight / n_splits
        rounded_weights = [round(split_weight) for _ in range(n_splits)]
        rounded_total = sum(rounded_weights)
        scrap = rounded_total - slit_weight if rounded_total > slit_weight else slit_weight - rounded_total
        total_scrap += scrap
    return cost, total_scrap

# pcikle and oil 150 pounds
# cut to length scrap weight 150

