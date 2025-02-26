export interface Bill {
  id: number;
  title: string;
  primary_sponsor: string;
}

export interface BillDetail {
  bill: Bill;
  supporters: number;
  opposers: number;
}