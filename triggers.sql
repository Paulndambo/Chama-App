##Mostly Tested On SQLite3
##Trigger To Populate Member Total Savings Table
#1. Option 1
CREATE TRIGGER populate_member_total_savings
AFTER INSERT ON data_member
FOR EACH ROW
BEGIN
	INSERT INTO finance_membertotalsaving(member_id, year, amount)
	VALUES(NEW.id_number, "2021", 0);
END

#2. Option 2
CREATE TRIGGER populate_member_total_savings
AFTER INSERT ON data_member
FOR EACH ROW
BEGIN
	INSERT INTO finance_membertotalsaving(member_id, year, amount)
	VALUES(NEW.id_number, NEW.year, 0);
END

#3. Option 3 => Using MembershipRenewal
CREATE TRIGGER populate_member_total_savings_after_membership_renewal
AFTER INSERT ON finance_membershiprenewal
FOR EACH ROW
BEGIN
	INSERT INTO finance_membertotalsaving (member_id, year, amount)
	VALUES (NEW.member_id, NEW.year, 0);
END

#4. Populating Member Total Savings
CREATE TRIGGER sum_member_total_savings
AFTER INSERT ON finance_saving
FOR EACH ROW
BEGIN
	UPDATE finance_membertotalsaving
	SET amount = amount + NEW.amount
	WHERE member_id = NEW.member_id AND year = NEW.year;
END


# Group Total Savings
##1. Group Total Savings Table Populating Using Group Registration
CREATE TRIGGER populate_group_total_savings
AFTER INSERT ON data_group
FOR EACH ROW
BEGIN
	INSERT INTO finance_grouptotalsaving(group_id, year, amount)
	VALUES (NEW.group_id, NEW.year, 0);
END

##2. Group Total Savings Table Populating Using Group Renewal
CREATE TRIGGER populate_group_total_savings_after_group_renewal
AFTER INSERT ON finance_grouprenewal
FOR EACH ROW
BEGIN
	INSERT INTO finance_grouptotalsaving(group_id, year, amount)
	VALUES(NEW.group_id, NEW.year, 0);
END


#3. Populating Group Total Savings
CREATE TRIGGER sum_group_total_savings
AFTER INSERT ON finance_groupsaving
FOR EACH ROW
BEGIN
	UPDATE finance_grouptotalsaving
	SET amount = amount + NEW.amount
	WHERE group_id = NEW.group_id AND year = NEW.year;
END
