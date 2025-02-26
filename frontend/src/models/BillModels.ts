export interface Bill {
  id: number;
  title: string;
}

export interface BillDetail {
  bill: Bill;
  supporters: number;
  opposers: number;
  primary_sponsor: string;
}