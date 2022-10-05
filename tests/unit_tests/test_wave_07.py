import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_newest():
    item_a = Clothing(age=1.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.age == pytest.approx(1.0)

# @pytest.mark.skip
def test_newest_with_duplicates():
    # Arrange
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    newest_item = tai.get_newest()

    # Assert
    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

# @pytest.mark.skip
def test_swap_newest():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_c, item_d]
    assert jesse.inventory == [item_e, item_f, item_a]
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other

# @pytest.mark.skip
def test_swap_newest_reordered():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_d]
    assert jesse.inventory == [item_f, item_e, item_a]
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

# @pytest.mark.skip
def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_newest_no_other_inventory_is_false():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory