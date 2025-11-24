/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     11/24/2025 1:50:40 AM                        */
/*==============================================================*/


/*==============================================================*/
/* Table: golongan_darah                                        */
/*==============================================================*/
create table golongan_darah
(
   golongan_id          INT not null auto_increment  comment '',
   golongan             VARCHAR(5)  comment '',
   tipe_golongan        VARCHAR(5)  comment '',
   primary key (golongan_id)
);

/*==============================================================*/
/* Table: jadwal_donor                                          */
/*==============================================================*/
create table jadwal_donor
(
   jadwal_id            INT not null auto_increment  comment '',
   tanggal              DATE  comment '',
   lokasi               VARCHAR(200)  comment '',
   keterangan           TEXT  comment '',
   primary key (jadwal_id)
);

/*==============================================================*/
/* Table: pendaftaran_donor                                     */
/*==============================================================*/
create table pendaftaran_donor
(
   daftar_id            INT not null auto_increment  comment '',
   jadwal_id            INT  comment '',
   pendonor_id          INT  comment '',
   status               VARCHAR(20) default 'menunggu'  comment '',
   tanggal_daftar       TIMESTAMP default CURRENT_TIMESTAMP  comment '',
   primary key (daftar_id)
);

/*==============================================================*/
/* Table: pengiriman_darah                                      */
/*==============================================================*/
create table pengiriman_darah
(
   kirim_id             INT not null auto_increment  comment '',
   permintaan_id        INT  comment '',
   stok_id              INT  comment '',
   jumlah_dikirim       INT  comment '',
   tanggal_kirim        TIMESTAMP default CURRENT_TIMESTAMP  comment '',
   petugas_id           INT  comment '',
   primary key (kirim_id)
);

/*==============================================================*/
/* Table: permintaan_rs                                         */
/*==============================================================*/
create table permintaan_rs
(
   permintaan_id        INT not null auto_increment  comment '',
   rs_id                INT  comment '',
   golongan_id          INT  comment '',
   jumlah_diminta       INT  comment '',
   status               VARCHAR(20) default 'menunggu'  comment '',
   tanggal_permintaan   TIMESTAMP default CURRENT_TIMESTAMP  comment '',
   primary key (permintaan_id)
);

/*==============================================================*/
/* Table: stok_darah                                            */
/*==============================================================*/
create table stok_darah
(
   stok_id              INT not null auto_increment  comment '',
   golongan_id          INT  comment '',
   jumlah_kantong       INT default 0  comment '',
   updated_at           TIMESTAMP default CURRENT_TIMESTAMP  comment '',
   primary key (stok_id)
);

/*==============================================================*/
/* Table: transaksi_darah                                       */
/*==============================================================*/
create table transaksi_darah
(
   transaksi_id         INT not null auto_increment  comment '',
   stok_id              INT  comment '',
   jenis_transaksi      VARCHAR(20)  comment '',
   jumlah               INT  comment '',
   tanggal              DATE  comment '',
   petugas_id           INT  comment '',
   primary key (transaksi_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   user_id              INT not null auto_increment  comment '',
   nama_lengkap         VARCHAR(100)  comment '',
   username             VARCHAR(100)  comment '',
   password             VARCHAR(200)  comment '',
   role                 VARCHAR(20)  comment '',
   alamat               TEXT  comment '',
   created_at           TIMESTAMP default CURRENT_TIMESTAMP  comment '',
   primary key (user_id)
);

alter table pendaftaran_donor add constraint FK_PENDAFTA_REFERENCE_JADWAL_D foreign key (jadwal_id)
      references jadwal_donor (jadwal_id);

alter table pendaftaran_donor add constraint FK_PENDAFTA_REFERENCE_USER foreign key (pendonor_id)
      references user (user_id);

alter table pengiriman_darah add constraint FK_PENGIRIM_REFERENCE_USER foreign key (petugas_id)
      references user (user_id);

alter table pengiriman_darah add constraint FK_PENGIRIM_REFERENCE_PERMINTA foreign key (permintaan_id)
      references permintaan_rs (permintaan_id);

alter table pengiriman_darah add constraint FK_PENGIRIM_REFERENCE_STOK_DAR foreign key (stok_id)
      references stok_darah (stok_id);

alter table permintaan_rs add constraint FK_PERMINTA_REFERENCE_USER foreign key (rs_id)
      references user (user_id);

alter table permintaan_rs add constraint FK_PERMINTA_REFERENCE_GOLONGAN foreign key (golongan_id)
      references golongan_darah (golongan_id);

alter table stok_darah add constraint FK_STOK_DAR_REFERENCE_GOLONGAN foreign key (golongan_id)
      references golongan_darah (golongan_id);

alter table transaksi_darah add constraint FK_TRANSAKS_REFERENCE_STOK_DAR foreign key (stok_id)
      references stok_darah (stok_id);

alter table transaksi_darah add constraint FK_TRANSAKS_REFERENCE_USER foreign key (petugas_id)
      references user (user_id);

