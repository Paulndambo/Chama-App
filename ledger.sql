CREATE TRIGGER log_fine_details
AFTER INSERT ON finance_fine
FOR EACH ROW
BEGIN
	INSERT INTO ledger_finelog(member_id, reason, amount_fined, date_fined)
	VALUES(NEW.member_id, NEW.reason, NEW.amount_fined, NEW.date_fined);
END

CREATE TRIGGER log_savings_details
AFTER INSERT ON finance_saving
FOR EACH ROW
BEGIN
	INSERT INTO ledger_savinglog(member_id, amount, date_submitted)
	VALUES(NEW.member_id, NEW.amount, NEW.date_submitted);
END

CREATE TRIGGER log_group_savings_details
AFTER INSERT ON finance_groupsaving
FOR EACH ROW
BEGIN
	INSERT INTO ledger_groupsavinglog(member_id, group_id, amount, year, date_paid)
	VALUES(NEW.member_id, NEW.group_id, NEW.amount, NEW.year, NEW.date_paid);
END

CREATE TRIGGER log_weekly_payment_details
AFTER INSERT ON finance_weeklypayment
FOR EACH ROW
BEGIN
	INSERT INTO ledger_weeklypaymentlog(member_id, amount, year, date_paid)
	VALUES(NEW.member_id, NEW.amount, NEW.year, NEW.date_paid);
END

CREATE TRIGGER log_group_renewal_details
AFTER INSERT ON finance_grouprenewal
FOR EACH ROW
BEGIN
	INSERT INTO ledger_grouprenewallog(group_id, amount_paid, year, date_paid)
	VALUES(NEW.group_id, NEW.amount_paid, NEW.year, NEW.date_paid);
END

CREATE TRIGGER log_group_registration_details
AFTER INSERT ON finance_groupregistration
FOR EACH ROW
BEGIN
	INSERT INTO ledger_groupregistrationlog(group_id, amount_paid, date_paid)
	VALUES(NEW.group_id, NEW.amount_paid, NEW.date_paid);
END

CREATE TRIGGER log_member_registration_fee_details
AFTER INSERT ON finance_memberregistration
FOR EACH ROW
BEGIN
	INSERT INTO ledger_memberregistrationlog(member_id, amount_paid, date_paid)
	VALUES(NEW.member_id, NEW.amount_paid, NEW.date_paid);
END

CREATE TRIGGER log_membership_renewal_details
AFTER INSERT ON finance_membershiprenewal
FOR EACH ROW
BEGIN
	INSERT INTO ledger_membershiprenewallog(member_id, renewal_amount, renewal_date)
	VALUES(NEW.member_id, NEW.renewal_amount, NEW.date_renewed);
END